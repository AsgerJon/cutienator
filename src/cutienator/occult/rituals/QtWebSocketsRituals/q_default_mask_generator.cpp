//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qdefaultmaskgenerator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qdefaultmaskgenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/private/qdefaultmaskgenerator_p.h>
#include <QtCore/QRandomGenerator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 52, as _ZN21QDefaultMaskGenerator4seedEv
inline bool QDefaultMaskGenerator::seed() noexcept
{
    return true;
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 62, as _ZN21QDefaultMaskGenerator8nextMaskEv
inline quint32 QDefaultMaskGenerator::nextMask() noexcept
{
    quint32 value = QRandomGenerator::global()->generate();
    while (Q_UNLIKELY(value == 0)) {
        // a mask of zero has a special meaning
        value = QRandomGenerator::global()->generate();
    }
    return value;
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 45, as _ZN21QDefaultMaskGeneratorD2Ev
inline QDefaultMaskGenerator::~QDefaultMaskGenerator()
{
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 35, as _ZN21QDefaultMaskGeneratorC1EP7QObject
inline QDefaultMaskGenerator::QDefaultMaskGenerator(QObject *parent) :
    QMaskGenerator(parent)
{
}
//  -----------------------------------------------------------------------

//  A QDefaultMaskGenerator that Python can take functions over in. Every QDefaultMaskGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDefaultMaskGeneratorCall0)(const void *, int *);
typedef quint32 (*CuteQDefaultMaskGeneratorCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDefaultMaskGeneratorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDefaultMaskGeneratorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultMaskGeneratorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultMaskGeneratorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultMaskGeneratorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultMaskGeneratorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultMaskGeneratorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDefaultMaskGenerator : public QDefaultMaskGenerator {
public:
  using QDefaultMaskGenerator::QDefaultMaskGenerator;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QMaskGenerator4seedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QMaskGenerator8nextMaskEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QDefaultMaskGenerator::seed()
  bool seed() noexcept override {
    if (taken[0]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall0 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDefaultMaskGenerator::seed();
  }

  //  quint32 QDefaultMaskGenerator::nextMask()
  quint32 nextMask() noexcept override {
    if (taken[1]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall1 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall1>(taken[1]);
      quint32 given = call(this, &handled);
      if (handled) return given;
    }
    return QDefaultMaskGenerator::nextMask();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall2 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall3 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall4 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall5 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall6 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall7 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDefaultMaskGeneratorCall8 call = reinterpret_cast<CuteQDefaultMaskGeneratorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QDefaultMaskGenerator::QDefaultMaskGenerator(QObject *parent)
extern "C" Q_DECL_EXPORT
QDefaultMaskGenerator *ritual_ZN21QDefaultMaskGeneratorC1EP7QObject(
    QObject *parent) {
  return new CuteQDefaultMaskGenerator(parent);
}

//  QDefaultMaskGenerator::~QDefaultMaskGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDefaultMaskGeneratorD1Ev(QDefaultMaskGenerator *self) {
  delete self;
}

//  bool QDefaultMaskGenerator::seed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QDefaultMaskGenerator4seedEv(QDefaultMaskGenerator *self) {
  return self->seed();
}

//  quint32 QDefaultMaskGenerator::nextMask()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN21QDefaultMaskGenerator8nextMaskEv(
    QDefaultMaskGenerator *self) {
  return self->nextMask();
}

//  a Python function taken by a CuteQDefaultMaskGenerator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDefaultMaskGenerator(
    QDefaultMaskGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDefaultMaskGenerator *>(self)->take(key, call);
}

//  bool QDefaultMaskGenerator::seed()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QDefaultMaskGenerator4seedEv(
    QDefaultMaskGenerator *self) {
  return self->QDefaultMaskGenerator::seed();
}

//  quint32 QDefaultMaskGenerator::nextMask()
extern "C" Q_DECL_EXPORT
quint32 ritual_own_ZN21QDefaultMaskGenerator8nextMaskEv(
    QDefaultMaskGenerator *self) {
  return self->QDefaultMaskGenerator::nextMask();
}
