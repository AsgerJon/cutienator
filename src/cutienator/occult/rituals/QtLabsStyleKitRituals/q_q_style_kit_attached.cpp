//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekit_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitreader_p.h>
#include <QtGui/QStyleHints>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekit.cpp, line 112, as _ZN18QQStyleKitAttachedD1Ev
inline QQStyleKitAttached::~QQStyleKitAttached()
{
    QQStyleKitAttached::s_instance = nullptr;
    if (m_ownsStyle) {
        delete m_style;
        m_style = nullptr;
    }
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekit.cpp, line 121, as _ZNK18QQStyleKitAttached5styleEv
inline QQStyleKitStyle *QQStyleKitAttached::style() const
{
    return m_style;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekit.cpp, line 140, as _ZNK18QQStyleKitAttached8styleUrlEv
inline QUrl QQStyleKitAttached::styleUrl() const
{
    return m_styleUrl;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekit.cpp, line 197, as _ZNK18QQStyleKitAttached5debugEv
inline QQStyleKitDebug *QQStyleKitAttached::debug() const
{
    return &const_cast<QQStyleKitAttached *>(this)->m_debug;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekit.cpp, line 202, as _ZNK18QQStyleKitAttached11styleLoadedEv
inline bool QQStyleKitAttached::styleLoaded() const
{
    return m_style && m_style->loaded();
}
//  -----------------------------------------------------------------------

//  A QQStyleKitAttached that Python can take functions over in. Every QQStyleKitAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQStyleKitAttached : public QQStyleKitAttached {
public:
  using QQStyleKitAttached::QQStyleKitAttached;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall0 call = reinterpret_cast<CuteQQStyleKitAttachedCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall1 call = reinterpret_cast<CuteQQStyleKitAttachedCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall2 call = reinterpret_cast<CuteQQStyleKitAttachedCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall3 call = reinterpret_cast<CuteQQStyleKitAttachedCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall4 call = reinterpret_cast<CuteQQStyleKitAttachedCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall5 call = reinterpret_cast<CuteQQStyleKitAttachedCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQStyleKitAttachedCall6 call = reinterpret_cast<CuteQQStyleKitAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQStyleKitAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQStyleKitAttached10metaObjectEv(
    const QQStyleKitAttached *self) {
  return self->metaObject();
}

//  void *QQStyleKitAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQStyleKitAttached11qt_metacastEPKc(
    QQStyleKitAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitAttached::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQStyleKitAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQStyleKitAttached::~QQStyleKitAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitAttachedD1Ev(QQStyleKitAttached *self) {
  delete self;
}

//  QQStyleKitStyle *QQStyleKitAttached::style() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK18QQStyleKitAttached5styleEv(
    const QQStyleKitAttached *self) {
  return self->style();
}

//  QUrl QQStyleKitAttached::styleUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQStyleKitAttached8styleUrlEv(
    const QQStyleKitAttached *self) {
  return new QUrl(self->styleUrl());
}

//  QQStyleKitDebug *QQStyleKitAttached::debug() const
extern "C" Q_DECL_EXPORT
QQStyleKitDebug *ritual_ZNK18QQStyleKitAttached5debugEv(
    const QQStyleKitAttached *self) {
  return self->debug();
}

//  bool QQStyleKitAttached::styleLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQStyleKitAttached11styleLoadedEv(
    const QQStyleKitAttached *self) {
  return self->styleLoaded();
}

//  void QQStyleKitAttached::styleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitAttached12styleChangedEv(
    QQStyleKitAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "styleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "styleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitAttached::styleUrlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitAttached15styleUrlChangedEv(
    QQStyleKitAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "styleUrlChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "styleUrlChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitAttached::transitionsEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitAttached25transitionsEnabledChangedEv(
    QQStyleKitAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "transitionsEnabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "transitionsEnabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQStyleKitAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQStyleKitAttached(
    QQStyleKitAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQStyleKitAttached *>(self)->take(key, call);
}
