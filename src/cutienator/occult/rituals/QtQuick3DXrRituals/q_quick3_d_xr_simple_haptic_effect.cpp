//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DXr/6.
//  12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 49, as _ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv
inline float QQuick3DXrSimpleHapticEffect::amplitude()
{
    return m_amplitude;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 67, as _ZN28QQuick3DXrSimpleHapticEffect8durationEv
inline float QQuick3DXrSimpleHapticEffect::duration()
{
    return m_duration;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 86, as _ZN28QQuick3DXrSimpleHapticEffect9frequencyEv
inline float QQuick3DXrSimpleHapticEffect::frequency()
{
    return m_frequency;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrSimpleHapticEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DXrSimpleHapticEffect10metaObjectEv(
    const QQuick3DXrSimpleHapticEffect *self) {
  return self->metaObject();
}

//  void *QQuick3DXrSimpleHapticEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuick3DXrSimpleHapticEffect11qt_metacastEPKc(
    QQuick3DXrSimpleHapticEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrSimpleHapticEffect::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuick3DXrSimpleHapticEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrSimpleHapticEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  float QQuick3DXrSimpleHapticEffect::amplitude()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->amplitude();
}

//  float QQuick3DXrSimpleHapticEffect::duration()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect8durationEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->duration();
}

//  float QQuick3DXrSimpleHapticEffect::frequency()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect9frequencyEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->frequency();
}

//  void QQuick3DXrSimpleHapticEffect::amplitudeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect16amplitudeChangedEv(
    QQuick3DXrSimpleHapticEffect *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSimpleHapticEffect")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "amplitudeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "amplitudeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSimpleHapticEffect::durationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect15durationChangedEv(
    QQuick3DXrSimpleHapticEffect *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSimpleHapticEffect")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "durationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "durationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSimpleHapticEffect::frequencyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect16frequencyChangedEv(
    QQuick3DXrSimpleHapticEffect *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSimpleHapticEffect")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "frequencyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "frequencyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
