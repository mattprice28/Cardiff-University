/**
 * Copyright 2010 JogAmp Community. All rights reserved.
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

package com.jogamp.opengl.test.junit.jogl.util.texture;


import com.jogamp.opengl.test.junit.jogl.demos.es2.GearsES2;
import com.jogamp.opengl.test.junit.util.MiscUtils;
import com.jogamp.opengl.test.junit.util.UITestCase;

import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.awt.GLCanvas;
import javax.swing.ImageIcon;
import javax.swing.JLabel;

import com.jogamp.opengl.util.FPSAnimator;
import com.jogamp.opengl.util.awt.AWTGLReadBufferUtil;

import java.awt.Frame;
import java.awt.image.BufferedImage;

import java.io.IOException;
import org.junit.Assert;
import org.junit.Assume;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;

/**
 * Demonstrates TextureData w/ AWT usage,
 * i.e. reading out an animated GL framebuffer and displaying it
 * as an BufferedImage.
 */
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class TestTexture02AWT extends UITestCase {
    static long durationPerTest = 500;
    static GLProfile glp;
    static GLCapabilities caps;

    @BeforeClass
    public static void initClass() {
        if(!GLProfile.isAvailable(GLProfile.GL2ES2)) {
            UITestCase.setTestSupported(false);
            return;
        }
        glp = GLProfile.getGL2ES2();
        Assert.assertNotNull(glp);
        caps = new GLCapabilities(glp);
        Assert.assertNotNull(caps);
    }

    @Test
    public void test1() throws InterruptedException {
        final AWTGLReadBufferUtil awtGLReadBufferUtil = new AWTGLReadBufferUtil(caps.getGLProfile(), false);
        final Frame frame0 = new Frame("GL -> AWT");
        final ImageIcon imageIcon = new ImageIcon();
        final JLabel imageLabel = new JLabel(imageIcon);
        frame0.add(imageLabel);

        final GLCanvas glCanvas = new GLCanvas(caps);
        final Frame frame1 = new Frame("GearsES2");
        Assert.assertNotNull(frame1);
        frame1.add(glCanvas);

        glCanvas.addGLEventListener(new GearsES2(1));
        glCanvas.addGLEventListener(new GLEventListener() {
            @Override
            public void init(final GLAutoDrawable drawable) { }
            @Override
            public void dispose(final GLAutoDrawable drawable) { }
            @Override
            public void display(final GLAutoDrawable drawable) {
                final BufferedImage outputImage = awtGLReadBufferUtil.readPixelsToBufferedImage(drawable.getGL(), true /* awtOrientation */);
                imageIcon.setImage(outputImage);
                imageLabel.repaint();
            }

            @Override
            public void reshape(final GLAutoDrawable drawable, final int x, final int y, final int width, final int height) {
                frame0.setSize(frame1.getWidth(), frame1.getHeight());
                frame0.setLocation(frame1.getX()+frame1.getWidth()+32, frame0.getY());
                frame0.validate();
            }
        });

        try {
            javax.swing.SwingUtilities.invokeAndWait(new Runnable() {
                public void run() {
                    frame1.setSize(256, 256);
                    frame1.setLocation(0, 0);
                    frame1.setVisible(true);
                    frame0.setSize(frame1.getWidth(), frame1.getHeight());
                    frame0.setLocation(frame1.getX()+frame1.getWidth()+32, frame0.getY());
                    frame0.setVisible(true);
                }});
        } catch( final Throwable throwable ) {
            throwable.printStackTrace();
            Assume.assumeNoException( throwable );
        }
        final FPSAnimator animator = new FPSAnimator(glCanvas, 15); // 15fps
        animator.start();

        Thread.sleep(durationPerTest);

        animator.stop();
        try {
            javax.swing.SwingUtilities.invokeAndWait(new Runnable() {
                public void run() {
                    frame0.setVisible(false);
                    frame0.dispose();
                    frame1.setVisible(false);
                    frame1.dispose();
                }});
        } catch( final Throwable throwable ) {
            throwable.printStackTrace();
            Assume.assumeNoException( throwable );
        }
    }

    public static void main(final String args[]) throws IOException {
        for(int i=0; i<args.length; i++) {
            if(args[i].equals("-time")) {
                durationPerTest = MiscUtils.atol(args[++i], durationPerTest);
            }
        }
        final String tstname = TestTexture02AWT.class.getName();
        org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner.main(new String[] {
            tstname,
            "filtertrace=true",
            "haltOnError=false",
            "haltOnFailure=false",
            "showoutput=true",
            "outputtoformatters=true",
            "logfailedtests=true",
            "logtestlistenerevents=true",
            "formatter=org.apache.tools.ant.taskdefs.optional.junit.PlainJUnitResultFormatter",
            "formatter=org.apache.tools.ant.taskdefs.optional.junit.XMLJUnitResultFormatter,TEST-"+tstname+".xml" } );
    }
}
