//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qabstractitemmodel.h>
#include <algorithm>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 248, as _ZN23QRemoteObjectSourceBaseD1Ev
inline QRemoteObjectSourceBase::~QRemoteObjectSourceBase()
{
    delete m_api;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 401, as _ZN23QRemoteObjectSourceBase6invokeEN11QMetaObject4CallEiRK5QListI8QVariantEPS3_
inline bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int index, const QVariantList &args, QVariant* returnValue)
{
    int status = -1;
    int flags = 0;
    bool forAdapter = (c == QMetaObject::InvokeMetaMethod ? m_api->isAdapterMethod(index) : m_api->isAdapterProperty(index));
    int resolvedIndex = (c == QMetaObject::InvokeMetaMethod ? m_api->sourceMethodIndex(index) : m_api->sourcePropertyIndex(index));
    if (resolvedIndex < 0)
        return false;
    QVarLengthArray<void*, 10> param(args.size() + 1);

    if (c == QMetaObject::InvokeMetaMethod) {
        QMetaMethod method;
        if (!forAdapter)
            method = parent()->metaObject()->method(resolvedIndex);

        if (returnValue) {
            if (!forAdapter && method.isValid() && method.returnType() == QMetaType::QVariant)
                param[0] = const_cast<void*>(reinterpret_cast<const void*>(returnValue));
            else
                param[0] = returnValue->data();
        } else {
            param[0] = nullptr;
        }

        auto argument = [&](int i) -> void * {
            if ((forAdapter && m_api->methodParameterType(index, i) == QMetaType::QVariant) ||
                    (method.isValid() && method.parameterType(i) == QMetaType::QVariant)) {
                return const_cast<void*>(reinterpret_cast<const void*>(&args.at(i)));
            }
            return const_cast<void*>(args.at(i).data());
        };

        for (int i = 0; i < args.size(); ++i) {
            param[i + 1] = argument(i);
        }
    } else if (c == QMetaObject::WriteProperty || c == QMetaObject::ReadProperty) {
        bool isQVariant = !forAdapter && parent()->metaObject()->property(resolvedIndex).userType() == QMetaType::QVariant;
        for (int i = 0; i < args.size(); ++i) {
            if (isQVariant)
                param[i] = const_cast<void*>(reinterpret_cast<const void*>(&args.at(i)));
            else
                param[i] = const_cast<void*>(args.at(i).data());
        }
        if (c == QMetaObject::WriteProperty) {
            Q_ASSERT(param.size() == 2); // for return-value and setter value
            // check QMetaProperty::write for an explanation of these
            param.append(&status);
            param.append(&flags);
        }
    } else {
        // Better safe than sorry
        return false;
    }
    int r = -1;
    if (forAdapter)
        r = m_adapter->qt_metacall(c, resolvedIndex, param.data());
    else
        r = parent()->qt_metacall(c, resolvedIndex, param.data());
    return r == -1 && status == -1;
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectSourceBase that Python can take functions over in. Every QRemoteObjectSourceBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQRemoteObjectSourceBaseCall0)(const void *, int *);
typedef bool (*CuteQRemoteObjectSourceBaseCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceBaseCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceBaseCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectSourceBase : public QRemoteObjectSourceBase {
public:
  using QRemoteObjectSourceBase::QRemoteObjectSourceBase;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase6isRootEv")) {
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

  //  QString QRemoteObjectSourceBase::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectSourceBaseCall0 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QRemoteObjectSourceBase::isRoot() const
  bool isRoot() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectSourceBaseCall1 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectSourceBaseCall2 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall2>(taken[2]);
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
      CuteQRemoteObjectSourceBaseCall3 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall3>(taken[3]);
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
      CuteQRemoteObjectSourceBaseCall4 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall4>(taken[4]);
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
      CuteQRemoteObjectSourceBaseCall5 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall5>(taken[5]);
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
      CuteQRemoteObjectSourceBaseCall6 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall6>(taken[6]);
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
      CuteQRemoteObjectSourceBaseCall7 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall7>(taken[7]);
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
      CuteQRemoteObjectSourceBaseCall8 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRemoteObjectSourceBase::~QRemoteObjectSourceBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRemoteObjectSourceBaseD1Ev(QRemoteObjectSourceBase *self) {
  delete self;
}

//  bool QRemoteObjectSourceBase::hasAdapter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRemoteObjectSourceBase10hasAdapterEv(
    const QRemoteObjectSourceBase *self) {
  return self->hasAdapter();
}

//  QString QRemoteObjectSourceBase::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRemoteObjectSourceBase4nameEv(
    const QRemoteObjectSourceBase *self) {
  return new QString(self->name());
}

//  bool QRemoteObjectSourceBase::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRemoteObjectSourceBase6isRootEv(
    const QRemoteObjectSourceBase *self) {
  return self->isRoot();
}

//  bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int index,
//      const QVariantList &args, QVariant *returnValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QRemoteObjectSourceBase6invokeEN11QMetaObject4CallEiRK5QListI8QVariantEPS3_(
    QRemoteObjectSourceBase *self,
    QMetaObject::Call c,
    int index,
    const QList<QVariant> *args,
    QVariant *returnValue) {
  return self->invoke(c, index, *args, returnValue);
}

//  a Python function taken by a CuteQRemoteObjectSourceBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectSourceBase(
    QRemoteObjectSourceBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectSourceBase *>(self)->take(key, call);
}
