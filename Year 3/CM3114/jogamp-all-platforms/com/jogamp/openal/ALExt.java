/* !---- DO NOT EDIT: This file autogenerated by com/jogamp/gluegen/procaddress/ProcAddressEmitter.java on Fri Oct 09 06:31:53 CEST 2015 ----! */

package com.jogamp.openal;

import java.io.UnsupportedEncodingException;
import java.util.*;
import com.jogamp.openal.*;
import jogamp.openal.*;
import java.security.AccessController;
import java.security.PrivilegedAction;
import com.jogamp.gluegen.runtime.*;
import com.jogamp.common.os.*;
import com.jogamp.common.nio.*;
import java.nio.*;

public interface ALExt extends ALExtConstants{


  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alBufferDataStatic(const ALint buffer, ALenum format, ALvoid *  data, ALsizei len, ALsizei freq)</code><br>
      @param data a direct or array-backed {@link java.nio.Buffer}   */
  public void alBufferDataStatic(int buffer, int format, Buffer data, int len, int freq);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGenEffects(ALsizei n, ALuint *  effects)</code><br>
      @param effects a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGenEffects(int n, IntBuffer effects);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGenEffects(ALsizei n, ALuint *  effects)</code><br>   */
  public void alGenEffects(int n, int[] effects, int effects_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alDeleteEffects(ALsizei n, const ALuint *  effects)</code><br>
      @param effects a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alDeleteEffects(int n, IntBuffer effects);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alDeleteEffects(ALsizei n, const ALuint *  effects)</code><br>   */
  public void alDeleteEffects(int n, int[] effects, int effects_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALboolean alIsEffect(ALuint effect)</code><br>   */
  public boolean alIsEffect(int effect);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alEffecti(ALuint effect, ALenum param, ALint iValue)</code><br>   */
  public void alEffecti(int effect, int param, int iValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alEffectiv(ALuint effect, ALenum param, const ALint *  piValues)</code><br>
      @param piValues a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alEffectiv(int effect, int param, IntBuffer piValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alEffectiv(ALuint effect, ALenum param, const ALint *  piValues)</code><br>   */
  public void alEffectiv(int effect, int param, int[] piValues, int piValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alEffectf(ALuint effect, ALenum param, ALfloat flValue)</code><br>   */
  public void alEffectf(int effect, int param, float flValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alEffectfv(ALuint effect, ALenum param, const ALfloat *  pflValues)</code><br>
      @param pflValues a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alEffectfv(int effect, int param, FloatBuffer pflValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alEffectfv(ALuint effect, ALenum param, const ALfloat *  pflValues)</code><br>   */
  public void alEffectfv(int effect, int param, float[] pflValues, int pflValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffecti(ALuint effect, ALenum param, ALint *  piValue)</code><br>
      @param piValue a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGetEffecti(int effect, int param, IntBuffer piValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffecti(ALuint effect, ALenum param, ALint *  piValue)</code><br>   */
  public void alGetEffecti(int effect, int param, int[] piValue, int piValue_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffectiv(ALuint effect, ALenum param, ALint *  piValues)</code><br>
      @param piValues a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGetEffectiv(int effect, int param, IntBuffer piValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffectiv(ALuint effect, ALenum param, ALint *  piValues)</code><br>   */
  public void alGetEffectiv(int effect, int param, int[] piValues, int piValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffectf(ALuint effect, ALenum param, ALfloat *  pflValue)</code><br>
      @param pflValue a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alGetEffectf(int effect, int param, FloatBuffer pflValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffectf(ALuint effect, ALenum param, ALfloat *  pflValue)</code><br>   */
  public void alGetEffectf(int effect, int param, float[] pflValue, int pflValue_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffectfv(ALuint effect, ALenum param, ALfloat *  pflValues)</code><br>
      @param pflValues a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alGetEffectfv(int effect, int param, FloatBuffer pflValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetEffectfv(ALuint effect, ALenum param, ALfloat *  pflValues)</code><br>   */
  public void alGetEffectfv(int effect, int param, float[] pflValues, int pflValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGenFilters(ALsizei n, ALuint *  filters)</code><br>
      @param filters a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGenFilters(int n, IntBuffer filters);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGenFilters(ALsizei n, ALuint *  filters)</code><br>   */
  public void alGenFilters(int n, int[] filters, int filters_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alDeleteFilters(ALsizei n, const ALuint *  filters)</code><br>
      @param filters a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alDeleteFilters(int n, IntBuffer filters);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alDeleteFilters(ALsizei n, const ALuint *  filters)</code><br>   */
  public void alDeleteFilters(int n, int[] filters, int filters_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALboolean alIsFilter(ALuint filter)</code><br>   */
  public boolean alIsFilter(int filter);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alFilteri(ALuint filter, ALenum param, ALint iValue)</code><br>   */
  public void alFilteri(int filter, int param, int iValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alFilteriv(ALuint filter, ALenum param, const ALint *  piValues)</code><br>
      @param piValues a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alFilteriv(int filter, int param, IntBuffer piValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alFilteriv(ALuint filter, ALenum param, const ALint *  piValues)</code><br>   */
  public void alFilteriv(int filter, int param, int[] piValues, int piValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alFilterf(ALuint filter, ALenum param, ALfloat flValue)</code><br>   */
  public void alFilterf(int filter, int param, float flValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alFilterfv(ALuint filter, ALenum param, const ALfloat *  pflValues)</code><br>
      @param pflValues a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alFilterfv(int filter, int param, FloatBuffer pflValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alFilterfv(ALuint filter, ALenum param, const ALfloat *  pflValues)</code><br>   */
  public void alFilterfv(int filter, int param, float[] pflValues, int pflValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilteri(ALuint filter, ALenum param, ALint *  piValue)</code><br>
      @param piValue a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGetFilteri(int filter, int param, IntBuffer piValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilteri(ALuint filter, ALenum param, ALint *  piValue)</code><br>   */
  public void alGetFilteri(int filter, int param, int[] piValue, int piValue_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilteriv(ALuint filter, ALenum param, ALint *  piValues)</code><br>
      @param piValues a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGetFilteriv(int filter, int param, IntBuffer piValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilteriv(ALuint filter, ALenum param, ALint *  piValues)</code><br>   */
  public void alGetFilteriv(int filter, int param, int[] piValues, int piValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilterf(ALuint filter, ALenum param, ALfloat *  pflValue)</code><br>
      @param pflValue a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alGetFilterf(int filter, int param, FloatBuffer pflValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilterf(ALuint filter, ALenum param, ALfloat *  pflValue)</code><br>   */
  public void alGetFilterf(int filter, int param, float[] pflValue, int pflValue_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilterfv(ALuint filter, ALenum param, ALfloat *  pflValues)</code><br>
      @param pflValues a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alGetFilterfv(int filter, int param, FloatBuffer pflValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetFilterfv(ALuint filter, ALenum param, ALfloat *  pflValues)</code><br>   */
  public void alGetFilterfv(int filter, int param, float[] pflValues, int pflValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGenAuxiliaryEffectSlots(ALsizei n, ALuint *  effectslots)</code><br>
      @param effectslots a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGenAuxiliaryEffectSlots(int n, IntBuffer effectslots);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGenAuxiliaryEffectSlots(ALsizei n, ALuint *  effectslots)</code><br>   */
  public void alGenAuxiliaryEffectSlots(int n, int[] effectslots, int effectslots_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alDeleteAuxiliaryEffectSlots(ALsizei n, const ALuint *  effectslots)</code><br>
      @param effectslots a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alDeleteAuxiliaryEffectSlots(int n, IntBuffer effectslots);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alDeleteAuxiliaryEffectSlots(ALsizei n, const ALuint *  effectslots)</code><br>   */
  public void alDeleteAuxiliaryEffectSlots(int n, int[] effectslots, int effectslots_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALboolean alIsAuxiliaryEffectSlot(ALuint effectslot)</code><br>   */
  public boolean alIsAuxiliaryEffectSlot(int effectslot);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alAuxiliaryEffectSloti(ALuint effectslot, ALenum param, ALint iValue)</code><br>   */
  public void alAuxiliaryEffectSloti(int effectslot, int param, int iValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alAuxiliaryEffectSlotiv(ALuint effectslot, ALenum param, const ALint *  piValues)</code><br>
      @param piValues a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alAuxiliaryEffectSlotiv(int effectslot, int param, IntBuffer piValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alAuxiliaryEffectSlotiv(ALuint effectslot, ALenum param, const ALint *  piValues)</code><br>   */
  public void alAuxiliaryEffectSlotiv(int effectslot, int param, int[] piValues, int piValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alAuxiliaryEffectSlotf(ALuint effectslot, ALenum param, ALfloat flValue)</code><br>   */
  public void alAuxiliaryEffectSlotf(int effectslot, int param, float flValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alAuxiliaryEffectSlotfv(ALuint effectslot, ALenum param, const ALfloat *  pflValues)</code><br>
      @param pflValues a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alAuxiliaryEffectSlotfv(int effectslot, int param, FloatBuffer pflValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alAuxiliaryEffectSlotfv(ALuint effectslot, ALenum param, const ALfloat *  pflValues)</code><br>   */
  public void alAuxiliaryEffectSlotfv(int effectslot, int param, float[] pflValues, int pflValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSloti(ALuint effectslot, ALenum param, ALint *  piValue)</code><br>
      @param piValue a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGetAuxiliaryEffectSloti(int effectslot, int param, IntBuffer piValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSloti(ALuint effectslot, ALenum param, ALint *  piValue)</code><br>   */
  public void alGetAuxiliaryEffectSloti(int effectslot, int param, int[] piValue, int piValue_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSlotiv(ALuint effectslot, ALenum param, ALint *  piValues)</code><br>
      @param piValues a direct or array-backed {@link java.nio.IntBuffer}   */
  public void alGetAuxiliaryEffectSlotiv(int effectslot, int param, IntBuffer piValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSlotiv(ALuint effectslot, ALenum param, ALint *  piValues)</code><br>   */
  public void alGetAuxiliaryEffectSlotiv(int effectslot, int param, int[] piValues, int piValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSlotf(ALuint effectslot, ALenum param, ALfloat *  pflValue)</code><br>
      @param pflValue a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alGetAuxiliaryEffectSlotf(int effectslot, int param, FloatBuffer pflValue);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSlotf(ALuint effectslot, ALenum param, ALfloat *  pflValue)</code><br>   */
  public void alGetAuxiliaryEffectSlotf(int effectslot, int param, float[] pflValue, int pflValue_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSlotfv(ALuint effectslot, ALenum param, ALfloat *  pflValues)</code><br>
      @param pflValues a direct or array-backed {@link java.nio.FloatBuffer}   */
  public void alGetAuxiliaryEffectSlotfv(int effectslot, int param, FloatBuffer pflValues);

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alGetAuxiliaryEffectSlotfv(ALuint effectslot, ALenum param, ALfloat *  pflValues)</code><br>   */
  public void alGetAuxiliaryEffectSlotfv(int effectslot, int param, float[] pflValues, int pflValues_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>ALCboolean alcSetThreadContext(ALCcontext *  context)</code><br>   */
  public boolean alcSetThreadContext(ALCcontext context);

  /** Entry point (through function pointer) to C language function: <br> <code>ALCcontext *  alcGetThreadContext(void)</code><br>   */
  public ALCcontext alcGetThreadContext();

  /** Entry point (through function pointer) to C language function: <br> <code>ALvoid alBufferSubDataSOFT(ALuint buffer, ALenum format, const ALvoid *  data, ALsizei offset, ALsizei length)</code><br>
      @param data a direct or array-backed {@link java.nio.Buffer}   */
  public void alBufferSubDataSOFT(int buffer, int format, Buffer data, int offset, int length);

  /** Entry point (through function pointer) to C language function: <br> <code>void alBufferSamplesSOFT(ALuint buffer, ALuint samplerate, ALenum internalformat, ALsizei samples, ALenum channels, ALenum type, const ALvoid *  data)</code><br>
      @param data a direct or array-backed {@link java.nio.Buffer}   */
  public void alBufferSamplesSOFT(int buffer, int samplerate, int internalformat, int samples, int channels, int type, Buffer data);

  /** Entry point (through function pointer) to C language function: <br> <code>void alBufferSubSamplesSOFT(ALuint buffer, ALsizei offset, ALsizei samples, ALenum channels, ALenum type, const ALvoid *  data)</code><br>
      @param data a direct or array-backed {@link java.nio.Buffer}   */
  public void alBufferSubSamplesSOFT(int buffer, int offset, int samples, int channels, int type, Buffer data);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetBufferSamplesSOFT(ALuint buffer, ALsizei offset, ALsizei samples, ALenum channels, ALenum type, ALvoid *  data)</code><br>
      @param data a direct or array-backed {@link java.nio.Buffer}   */
  public void alGetBufferSamplesSOFT(int buffer, int offset, int samples, int channels, int type, Buffer data);

  /** Entry point (through function pointer) to C language function: <br> <code>ALboolean alIsBufferFormatSupportedSOFT(ALenum format)</code><br>   */
  public boolean alIsBufferFormatSupportedSOFT(int format);

  /** Entry point (through function pointer) to C language function: <br> <code>ALCdevice *  alcLoopbackOpenDeviceSOFT(const ALCchar *  deviceName)</code><br>   */
  public ALCdevice alcLoopbackOpenDeviceSOFT(String deviceName);

  /** Entry point (through function pointer) to C language function: <br> <code>ALCboolean alcIsRenderFormatSupportedSOFT(ALCdevice *  device, ALCsizei freq, ALCenum channels, ALCenum type)</code><br>   */
  public boolean alcIsRenderFormatSupportedSOFT(ALCdevice device, int freq, int channels, int type);

  /** Entry point (through function pointer) to C language function: <br> <code>void alcRenderSamplesSOFT(ALCdevice *  device, ALCvoid *  buffer, ALCsizei samples)</code><br>
      @param buffer a direct or array-backed {@link java.nio.Buffer}   */
  public void alcRenderSamplesSOFT(ALCdevice device, Buffer buffer, int samples);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSourcedSOFT(ALuint source, ALenum param, ALdouble value)</code><br>   */
  public void alSourcedSOFT(int source, int param, double value);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSource3dSOFT(ALuint source, ALenum param, ALdouble value1, ALdouble value2, ALdouble value3)</code><br>   */
  public void alSource3dSOFT(int source, int param, double value1, double value2, double value3);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSourcedvSOFT(ALuint source, ALenum param, const ALdouble *  values)</code><br>
      @param values a direct or array-backed {@link java.nio.DoubleBuffer}   */
  public void alSourcedvSOFT(int source, int param, DoubleBuffer values);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSourcedvSOFT(ALuint source, ALenum param, const ALdouble *  values)</code><br>   */
  public void alSourcedvSOFT(int source, int param, double[] values, int values_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcedSOFT(ALuint source, ALenum param, ALdouble *  value)</code><br>
      @param value a direct or array-backed {@link java.nio.DoubleBuffer}   */
  public void alGetSourcedSOFT(int source, int param, DoubleBuffer value);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcedSOFT(ALuint source, ALenum param, ALdouble *  value)</code><br>   */
  public void alGetSourcedSOFT(int source, int param, double[] value, int value_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSource3dSOFT(ALuint source, ALenum param, ALdouble *  value1, ALdouble *  value2, ALdouble *  value3)</code><br>
      @param value1 a direct or array-backed {@link java.nio.DoubleBuffer}
      @param value2 a direct or array-backed {@link java.nio.DoubleBuffer}
      @param value3 a direct or array-backed {@link java.nio.DoubleBuffer}   */
  public void alGetSource3dSOFT(int source, int param, DoubleBuffer value1, DoubleBuffer value2, DoubleBuffer value3);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSource3dSOFT(ALuint source, ALenum param, ALdouble *  value1, ALdouble *  value2, ALdouble *  value3)</code><br>   */
  public void alGetSource3dSOFT(int source, int param, double[] value1, int value1_offset, double[] value2, int value2_offset, double[] value3, int value3_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcedvSOFT(ALuint source, ALenum param, ALdouble *  values)</code><br>
      @param values a direct or array-backed {@link java.nio.DoubleBuffer}   */
  public void alGetSourcedvSOFT(int source, int param, DoubleBuffer values);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcedvSOFT(ALuint source, ALenum param, ALdouble *  values)</code><br>   */
  public void alGetSourcedvSOFT(int source, int param, double[] values, int values_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSourcei64SOFT(ALuint source, ALenum param, ALint64SOFT value)</code><br>   */
  public void alSourcei64SOFT(int source, int param, long value);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSource3i64SOFT(ALuint source, ALenum param, ALint64SOFT value1, ALint64SOFT value2, ALint64SOFT value3)</code><br>   */
  public void alSource3i64SOFT(int source, int param, long value1, long value2, long value3);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSourcei64vSOFT(ALuint source, ALenum param, const ALint64SOFT *  values)</code><br>
      @param values a direct or array-backed {@link java.nio.LongBuffer}   */
  public void alSourcei64vSOFT(int source, int param, LongBuffer values);

  /** Entry point (through function pointer) to C language function: <br> <code>void alSourcei64vSOFT(ALuint source, ALenum param, const ALint64SOFT *  values)</code><br>   */
  public void alSourcei64vSOFT(int source, int param, long[] values, int values_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcei64SOFT(ALuint source, ALenum param, ALint64SOFT *  value)</code><br>
      @param value a direct or array-backed {@link java.nio.LongBuffer}   */
  public void alGetSourcei64SOFT(int source, int param, LongBuffer value);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcei64SOFT(ALuint source, ALenum param, ALint64SOFT *  value)</code><br>   */
  public void alGetSourcei64SOFT(int source, int param, long[] value, int value_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSource3i64SOFT(ALuint source, ALenum param, ALint64SOFT *  value1, ALint64SOFT *  value2, ALint64SOFT *  value3)</code><br>
      @param value1 a direct or array-backed {@link java.nio.LongBuffer}
      @param value2 a direct or array-backed {@link java.nio.LongBuffer}
      @param value3 a direct or array-backed {@link java.nio.LongBuffer}   */
  public void alGetSource3i64SOFT(int source, int param, LongBuffer value1, LongBuffer value2, LongBuffer value3);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSource3i64SOFT(ALuint source, ALenum param, ALint64SOFT *  value1, ALint64SOFT *  value2, ALint64SOFT *  value3)</code><br>   */
  public void alGetSource3i64SOFT(int source, int param, long[] value1, int value1_offset, long[] value2, int value2_offset, long[] value3, int value3_offset);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcei64vSOFT(ALuint source, ALenum param, ALint64SOFT *  values)</code><br>
      @param values a direct or array-backed {@link java.nio.LongBuffer}   */
  public void alGetSourcei64vSOFT(int source, int param, LongBuffer values);

  /** Entry point (through function pointer) to C language function: <br> <code>void alGetSourcei64vSOFT(ALuint source, ALenum param, ALint64SOFT *  values)</code><br>   */
  public void alGetSourcei64vSOFT(int source, int param, long[] values, int values_offset);


} // end of class ALExt
