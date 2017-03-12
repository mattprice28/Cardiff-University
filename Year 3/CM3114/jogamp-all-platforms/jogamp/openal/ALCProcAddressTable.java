/* !---- DO NOT EDIT: This file autogenerated by com/jogamp/gluegen/procaddress/ProcAddressEmitter.java on Fri Oct 09 06:31:43 CEST 2015 ----! */

package jogamp.openal;

import java.io.UnsupportedEncodingException;
import java.util.*;
import com.jogamp.openal.*;
import jogamp.openal.*;
import java.security.AccessController;
import java.security.PrivilegedAction;
import com.jogamp.gluegen.runtime.ProcAddressTable;
import com.jogamp.common.util.SecurityUtil;

/**
 * This table is a cache of pointers to the dynamically-linkable C library.
 * @see ProcAddressTable
 */
public final class ALCProcAddressTable extends ProcAddressTable {


  public ALCProcAddressTable(){ super(); }

  public ALCProcAddressTable(com.jogamp.gluegen.runtime.FunctionAddressResolver resolver){ super(resolver); }

  /* pp */ long _addressof_alcCreateContext;
  /* pp */ long _addressof_alcMakeContextCurrent;
  /* pp */ long _addressof_alcProcessContext;
  /* pp */ long _addressof_alcSuspendContext;
  /* pp */ long _addressof_alcDestroyContext;
  /* pp */ long _addressof_alcGetCurrentContext;
  /* pp */ long _addressof_alcGetContextsDevice;
  /* pp */ long _addressof_alcOpenDevice;
  /* pp */ long _addressof_alcCloseDevice;
  /* pp */ long _addressof_alcGetError;
  /* pp */ long _addressof_alcIsExtensionPresent;
  /* pp */ long _addressof_alcGetProcAddress;
  /* pp */ long _addressof_alcGetEnumValue;
  /* pp */ long _addressof_alcGetString;
  /* pp */ long _addressof_alcGetIntegerv;
  /* pp */ long _addressof_alcCaptureOpenDevice;
  /* pp */ long _addressof_alcCaptureCloseDevice;
  /* pp */ long _addressof_alcCaptureStart;
  /* pp */ long _addressof_alcCaptureStop;
  /* pp */ long _addressof_alcCaptureSamples;
} // end of class ALCProcAddressTable