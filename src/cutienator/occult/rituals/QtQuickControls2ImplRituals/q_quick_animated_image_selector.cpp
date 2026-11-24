//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickimageselector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickimageselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qproperty.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/private/qquickimageselector_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qdir.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qfileselector.h>
#include <QtCore/qloggingcategory.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlfile.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 181, as _ZN19QQuickImageSelector10classBeginEv
inline void QQuickImageSelector::classBegin()
{
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 185, as _ZN19QQuickImageSelector17componentCompleteEv
inline void QQuickImageSelector::componentComplete()
{
    setUrl(m_property.read().toUrl());
    m_complete = true;
    updateSource();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 171, as _ZN19QQuickImageSelector5writeERK8QVariant
inline void QQuickImageSelector::write(const QVariant &value)
{
    setUrl(value.toUrl());
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 176, as _ZN19QQuickImageSelector9setTargetERK12QQmlProperty
inline void QQuickImageSelector::setTarget(const QQmlProperty &property)
{
    m_property = property;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 312, as _ZNK27QQuickAnimatedImageSelector14fileExtensionsEv
inline QStringList QQuickAnimatedImageSelector::fileExtensions() const
{
    static const QStringList extensions = QStringList() << QStringLiteral("webp") << QStringLiteral("gif");
    return extensions;
}
//  -----------------------------------------------------------------------

//  A QQuickAnimatedImageSelector that Python can take functions over in. Every QQuickAnimatedImageSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAnimatedImageSelectorCall0)(const void *, const QVariant *, int *);
typedef void (*CuteQQuickAnimatedImageSelectorCall1)(const void *, const QQmlProperty *, int *);
typedef void (*CuteQQuickAnimatedImageSelectorCall2)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageSelectorCall3)(const void *, int *);
typedef bool (*CuteQQuickAnimatedImageSelectorCall4)(const void *, QUntypedBindable *, const QUntypedBindable *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatedImageSelectorCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatedImageSelectorCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageSelectorCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageSelectorCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageSelectorCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageSelectorCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageSelectorCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnimatedImageSelector : public QQuickAnimatedImageSelector {
public:
  using QQuickAnimatedImageSelector::QQuickAnimatedImageSelector;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor5writeERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor9setTargetERK12QQmlProperty")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindableS0_")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickImageSelector::write(const QVariant &value)
  void write(const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall0 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall0>(taken[0]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QQuickImageSelector::write(value);
  }

  //  void QQuickImageSelector::setTarget(const QQmlProperty &property)
  void setTarget(const QQmlProperty &property) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall1 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall1>(taken[1]);
      call(this, &property, &handled);
      if (handled) return;
    }
    QQuickImageSelector::setTarget(property);
  }

  //  void QQuickImageSelector::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall2 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageSelector::classBegin();
  }

  //  void QQuickImageSelector::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall3 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageSelector::componentComplete();
  }

  //  bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable
  //      *bindable, QUntypedBindable target)
  bool bindable(
      QUntypedBindable *bindable,
      QUntypedBindable target) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall4 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall4>(taken[4]);
      bool given = call(this, bindable, &target, &handled);
      if (handled) return given;
    }
    return QQmlPropertyValueInterceptor::bindable(bindable, target);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall5 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall6 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall7 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall8 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall9 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall10 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAnimatedImageSelectorCall11 call = reinterpret_cast<CuteQQuickAnimatedImageSelectorCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnimatedImageSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickAnimatedImageSelector10metaObjectEv(
    const QQuickAnimatedImageSelector *self) {
  return self->metaObject();
}

//  QStringList QQuickAnimatedImageSelector::fileExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK27QQuickAnimatedImageSelector14fileExtensionsEv(
    const QQuickAnimatedImageSelector *self) {
  return new QList<QString>(self->fileExtensions());
}

//  a Python function taken by a CuteQQuickAnimatedImageSelector, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatedImageSelector(
    QQuickAnimatedImageSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatedImageSelector *>(self)->take(key, call);
}
