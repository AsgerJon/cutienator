//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dnditem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_dnditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDesigner/abstractdnditem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A qdesigner_internal::QDesignerMimeData that Python can take functions over in. Every qdesigner_internal::QDesignerMimeData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*Cuteqdesigner_internal_QDesignerMimeDataCall0)(const void *, const QString *, int *);
typedef const QVariant * (*Cuteqdesigner_internal_QDesignerMimeDataCall1)(const void *, const QString *, const QMetaType *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerMimeDataCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerMimeDataCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerMimeDataCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerMimeDataCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerMimeDataCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerMimeDataCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerMimeDataCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_QDesignerMimeData : public qdesigner_internal::QDesignerMimeData {
public:
  using qdesigner_internal::QDesignerMimeData::QDesignerMimeData;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QMimeData9hasFormatERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QMimeData12retrieveDataERK7QString9QMetaType")) {
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

  //  bool QMimeData::hasFormat(const QString &mimetype) const
  bool hasFormat(const QString &mimetype) const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerMimeDataCall0 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall0>(taken[0]);
      bool given = call(this, &mimetype, &handled);
      if (handled) return given;
    }
    return QMimeData::hasFormat(mimetype);
  }

  //  QVariant QMimeData::retrieveData(const QString &mimetype, QMetaType
  //      preferredType) const
  QVariant retrieveData(
      const QString &mimetype,
      QMetaType preferredType) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerMimeDataCall1 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall1>(taken[1]);
      const QVariant * given = call(this, &mimetype, &preferredType, &handled);
      if (handled && given) return *given;
    }
    return QMimeData::retrieveData(mimetype, preferredType);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerMimeDataCall2 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall2>(taken[2]);
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
      Cuteqdesigner_internal_QDesignerMimeDataCall3 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall3>(taken[3]);
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
      Cuteqdesigner_internal_QDesignerMimeDataCall4 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall4>(taken[4]);
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
      Cuteqdesigner_internal_QDesignerMimeDataCall5 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall5>(taken[5]);
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
      Cuteqdesigner_internal_QDesignerMimeDataCall6 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall6>(taken[6]);
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
      Cuteqdesigner_internal_QDesignerMimeDataCall7 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall7>(taken[7]);
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
      Cuteqdesigner_internal_QDesignerMimeDataCall8 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerMimeDataCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::QDesignerMimeData::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17QDesignerMimeData10metaObjectEv(
    const qdesigner_internal::QDesignerMimeData *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::QDesignerMimeData::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17QDesignerMimeData2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QDesignerMimeData::tr(s, c, n));
}

//  const QDesignerDnDItems &qdesigner_internal::QDesignerMimeData::items()
//      const
extern "C" Q_DECL_EXPORT
QList<QDesignerDnDItemInterface *> *ritual_ZNK18qdesigner_internal17QDesignerMimeData5itemsEv(
    const qdesigner_internal::QDesignerMimeData *self) {
  return new QList<QDesignerDnDItemInterface *>(self->items());
}

//  QPoint qdesigner_internal::QDesignerMimeData::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18qdesigner_internal17QDesignerMimeData7hotSpotEv(
    const qdesigner_internal::QDesignerMimeData *self) {
  return new QPoint(self->hotSpot());
}

//  a Python function taken by a Cuteqdesigner_internal_QDesignerMimeData,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QDesignerMimeData(
    qdesigner_internal::QDesignerMimeData *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QDesignerMimeData *>(self)->take(key, call);
}
