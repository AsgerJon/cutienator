//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandinputmethodcontrol.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(im)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#include <QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h>
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtWaylandCompositor/qwaylandseat.h>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtWaylandCompositor/qwaylandtextinput.h>
#include <QtWaylandCompositor/qwaylandtextinputv3.h>
#include <QtWaylandCompositor/qwaylandqttextinputmethod.h>
#include <QtGui/QInputMethodEvent>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 84, as _ZNK26QWaylandInputMethodControl7enabledEv
inline bool QWaylandInputMethodControl::enabled() const
{
    Q_D(const QWaylandInputMethodControl);

    return d->enabled;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWaylandInputMethodControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWaylandInputMethodControl10metaObjectEv(
    const QWaylandInputMethodControl *self) {
  return self->metaObject();
}

//  void *QWaylandInputMethodControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWaylandInputMethodControl11qt_metacastEPKc(
    QWaylandInputMethodControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandInputMethodControl::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWaylandInputMethodControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandInputMethodControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QWaylandInputMethodControlPrivate *QWaylandInputMethodControl::d_func()
extern "C" Q_DECL_EXPORT
QWaylandInputMethodControlPrivate *ritual_ZN26QWaylandInputMethodControl6d_funcEv(
    QWaylandInputMethodControl *self) {
  return self->d_func();
}

//  const QWaylandInputMethodControlPrivate
//      *QWaylandInputMethodControl::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandInputMethodControlPrivate *ritual_ZNK26QWaylandInputMethodControl6d_funcEv(
    const QWaylandInputMethodControl *self) {
  return self->d_func();
}

//  bool QWaylandInputMethodControl::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWaylandInputMethodControl7enabledEv(
    const QWaylandInputMethodControl *self) {
  return self->enabled();
}

//  void QWaylandInputMethodControl::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl14enabledChangedEb(
    QWaylandInputMethodControl *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWaylandInputMethodControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWaylandInputMethodControl::updateInputMethod(Qt::InputMethodQueries
//      queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl17updateInputMethodE6QFlagsIN2Qt16InputMethodQueryEE(
    QWaylandInputMethodControl *self,
    int queries) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWaylandInputMethodControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateInputMethod(Qt::InputMethodQueries)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateInputMethod(Qt::InputMethodQueries)");
  Qt::InputMethodQueries value0 = QFlags<Qt::InputMethodQuery>::fromInt(queries);
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&value0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(im)
