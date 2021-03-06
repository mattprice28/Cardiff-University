/* !---- DO NOT EDIT: This file autogenerated by com/jogamp/gluegen/JavaEmitter.java on Fri Oct 09 06:32:03 CEST 2015 ----! */


package com.jogamp.openal;

import java.nio.*;

import com.jogamp.gluegen.runtime.*;
import com.jogamp.common.os.*;
import com.jogamp.common.nio.*;
import jogamp.common.os.MachineDataInfoRuntime;


public class ALCdevice {

  StructAccessor accessor;

  private static final int mdIdx = MachineDataInfoRuntime.getStatic().ordinal();
  private final MachineDataInfo md;

  private static final int[] ALCdevice_size = new int[] { 0 /* ARM_MIPS_32 */, 0 /* X86_32_UNIX */, 0 /* X86_32_MACOS */, 0 /* PPC_32_UNIX */, 0 /* SPARC_32_SUNOS */, 0 /* X86_32_WINDOWS */, 0 /* LP64_UNIX */, 0 /* X86_64_WINDOWS */  };

  public static int size() {
    return ALCdevice_size[mdIdx];
  }

  public static ALCdevice create() {
    return create(Buffers.newDirectByteBuffer(size()));
  }

  public static ALCdevice create(java.nio.ByteBuffer buf) {
      return new ALCdevice(buf);
  }

  ALCdevice(java.nio.ByteBuffer buf) {
    md = MachineDataInfo.StaticConfig.values()[mdIdx].md;
    accessor = new StructAccessor(buf);
  }

  public java.nio.ByteBuffer getBuffer() {
    return accessor.getBuffer();
  }
}
