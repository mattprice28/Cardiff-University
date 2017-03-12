/**
 * Copyright 2011 JogAmp Community. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification, are
 * permitted provided that the following conditions are met:
 *
 *    1. Redistributions of source code must retain the above copyright notice, this list of
 *       conditions and the following disclaimer.
 *
 *    2. Redistributions in binary form must reproduce the above copyright notice, this list
 *       of conditions and the following disclaimer in the documentation and/or other materials
 *       provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY JogAmp Community ``AS IS'' AND ANY EXPRESS OR IMPLIED
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
 * FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL JogAmp Community OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * The views and conclusions contained in the software and documentation are those of the
 * authors and should not be interpreted as representing official policies, either expressed
 * or implied, of JogAmp Community.
 */
package com.jogamp.opengl.test.junit.jogl.acore;

import com.jogamp.common.nio.Buffers;
import com.jogamp.opengl.test.junit.util.NEWTGLContext;
import com.jogamp.opengl.test.junit.util.UITestCase;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;

import com.jogamp.opengl.GL;
import com.jogamp.opengl.GL2ES3;
import com.jogamp.opengl.GLBufferStorage;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLProfile;

import org.junit.Assert;
import org.junit.Test;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;

/**
 * Verifies content of buffer storage's content
 * as well as general buffer- and buffer-storage tracking.
 * <p>
 * Implementation uses ByteBuffer and Buffers or NIO API.
 * </p>
 *
 * @author Luz, et.al.
 */
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class TestMapBufferRead01NEWT extends UITestCase {
    static final boolean DEBUG = false;

    @Test
    public void testWriteRead01aMap() throws InterruptedException {
        if(!GLProfile.isAvailable(GLProfile.GL2GL3)) {
            System.err.println("Test requires GL2/GL3 profile.");
            return;
        }
        testWriteRead01(createVerticesBB(false), false /* useRange */);
    }
    @Test
    public void testWriteRead01bMap() throws InterruptedException {
        if(!GLProfile.isAvailable(GLProfile.GL2GL3)) {
            System.err.println("Test requires GL2/GL3 profile.");
            return;
        }
        testWriteRead01(createVerticesBB(true), false /* useRange */);
    }

    @Test
    public void testWriteRead02aMapRange() throws InterruptedException {
        if(!GLProfile.isAvailable(GLProfile.GL3) && !!GLProfile.isAvailable(GLProfile.GLES3)) {
            System.err.println("Test requires GL3 or GLES3 profile.");
            return;
        }
        testWriteRead01(createVerticesBB(false), true/* useRange */);
    }
    @Test
    public void testWriteRead02bMapRange() throws InterruptedException {
        if(!GLProfile.isAvailable(GLProfile.GL3) && !!GLProfile.isAvailable(GLProfile.GLES3)) {
            System.err.println("Test requires GL3 or GLES3 profile.");
            return;
        }
        testWriteRead01(createVerticesBB(true), true /* useRange */);
    }

    static final float[] vertexData = new float[] { -0.3f, -0.2f, -0.1f, 0.1f, 0.2f, 0.3f, 0.4f, 0.5f, 0.6f };

    static ByteBuffer createVerticesBB(final boolean useBuffersAPI) {
        final ByteBuffer res;
        if( useBuffersAPI ) {
            res = Buffers.newDirectByteBuffer(Buffers.SIZEOF_FLOAT*vertexData.length);
            final FloatBuffer resF = res.asFloatBuffer();
            resF.put(vertexData, 0, vertexData.length).rewind();
        } else {
            res = ByteBuffer.allocate(Buffers.SIZEOF_FLOAT*vertexData.length);
            res.order(ByteOrder.nativeOrder());
            for(int i=0; i<vertexData.length; i++) {
                res.putFloat(vertexData[i]);
            }
            res.rewind();
        }
        if(DEBUG) {
            System.err.println("java "+res);
            for(int i=0; i < res.capacity(); i+=4) {
                System.err.println("java ["+i+"]: "+res.getFloat(i));
            }
        }
        return res;
    }

    private void testWriteRead01(final ByteBuffer verticiesBB, final boolean useRange) throws InterruptedException {
        // Validate incoming ByteBuffer first
        assertEquals(0, verticiesBB.position());
        assertEquals(Buffers.SIZEOF_FLOAT*vertexData.length, verticiesBB.limit());
        assertEquals(Buffers.SIZEOF_FLOAT*vertexData.length, verticiesBB.capacity());
        assertEquals(Buffers.SIZEOF_FLOAT*vertexData.length, verticiesBB.remaining());
        assertEquals(-0.3f, verticiesBB.getFloat(Buffers.SIZEOF_FLOAT*0), 0.05f);
        assertEquals( 0.6f, verticiesBB.getFloat(Buffers.SIZEOF_FLOAT*8), 0.05f);

        final GLProfile glp = GLProfile.getMaxProgrammable(true);
        final GLCapabilities caps = new GLCapabilities(glp);
        caps.setOnscreen(false);
        final NEWTGLContext.WindowContext winctx = NEWTGLContext.createWindow(
                caps, 800, 600, true);
        try {
            final GL gl = winctx.context.getGL();

            final int[] vertexBuffer = new int[1];

            gl.glGenBuffers(1, vertexBuffer, 0);

            gl.glBindBuffer(GL.GL_ARRAY_BUFFER, vertexBuffer[0]);

            gl.glBufferData(GL.GL_ARRAY_BUFFER, verticiesBB.capacity(), verticiesBB, GL2ES3.GL_STATIC_READ);
            // gl.glBufferData(GL.GL_ARRAY_BUFFER, verticiesBB.capacity(), verticiesBB, GL.GL_STATIC_DRAW);

            final int bufferName = gl.getBoundBuffer(GL.GL_ARRAY_BUFFER);
            final GLBufferStorage bufferStorage = gl.getBufferStorage(bufferName);
            System.err.println("gpu-01 GL_ARRAY_BUFFER -> bufferName "+bufferName+" -> "+bufferStorage);
            Assert.assertEquals("Buffer storage's bytes-buffer not null before map", null, bufferStorage.getMappedBuffer());

            final int floatOffset, byteOffset, mapByteLength;
            final ByteBuffer bb;
            if( useRange ) {
                floatOffset = 3;
                byteOffset = Buffers.SIZEOF_FLOAT*floatOffset;
                mapByteLength = verticiesBB.capacity()-byteOffset;
                bb = gl.glMapBufferRange(GL.GL_ARRAY_BUFFER, byteOffset, mapByteLength, GL.GL_MAP_READ_BIT);
            } else {
                floatOffset = 0;
                byteOffset = 0;
                mapByteLength = verticiesBB.capacity();
                bb = gl.glMapBuffer(GL.GL_ARRAY_BUFFER, GL2ES3.GL_READ_ONLY);
            }
            System.err.println("gpu-02 mapped GL_ARRAY_BUFFER, floatOffset "+floatOffset+", byteOffset "+byteOffset+", mapByteLength "+mapByteLength+" -> "+bb);
            System.err.println("gpu-03 GL_ARRAY_BUFFER -> bufferName "+bufferName+" -> "+bufferStorage);
            Assert.assertNotNull(bb);
            Assert.assertEquals("BufferStorage size less byteOffset not equals buffer storage size", bufferStorage.getSize()-byteOffset, bb.capacity());
            Assert.assertEquals("BufferStorage's bytes-buffer not equal with mapped bytes-buffer", bufferStorage.getMappedBuffer(), bb);
            Assert.assertEquals("Buffer storage size not equals mapByteLength", mapByteLength, bb.capacity());

            if(DEBUG) {
                System.err.println("floatOffset "+floatOffset+", byteOffset "+byteOffset);
                for(int i=0; i < bb.capacity(); i+=4) {
                    System.err.println("gpu "+i+": "+bb.getFloat(i));
                }
            }
            for(int i=0; i < bb.capacity(); i+=4) {
                Assert.assertEquals(verticiesBB.getFloat(byteOffset+i), bb.getFloat(i), 0.0001f);
            }
            gl.glUnmapBuffer(GL.GL_ARRAY_BUFFER);
            Assert.assertEquals("Buffer storage's bytes-buffer not null after unmap", null, bufferStorage.getMappedBuffer());
        } finally {
            NEWTGLContext.destroyWindow(winctx);
        }
    }
    public static void main(final String args[]) throws IOException {
        final String tstname = TestMapBufferRead01NEWT.class.getName();
        org.junit.runner.JUnitCore.main(tstname);
    }
}
