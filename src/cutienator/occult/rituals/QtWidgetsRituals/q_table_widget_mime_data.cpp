//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tablewidget)
#if QT_CONFIG(tablewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTableWidgetMimeData that Python can take functions over in. Every QTableWidgetMimeData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTableWidgetMimeDataCall0)(const void *, const QString *, int *);
typedef const QVariant * (*CuteQTableWidgetMimeDataCall1)(const void *, const QString *, const QMetaType *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTableWidgetMimeDataCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTableWidgetMimeDataCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetMimeDataCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetMimeDataCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetMimeDataCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetMimeDataCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetMimeDataCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTableWidgetMimeData : public QTableWidgetMimeData {
public:
  using QTableWidgetMimeData::QTableWidgetMimeData;
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
      CuteQTableWidgetMimeDataCall0 call = reinterpret_cast<CuteQTableWidgetMimeDataCall0>(taken[0]);
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
      CuteQTableWidgetMimeDataCall1 call = reinterpret_cast<CuteQTableWidgetMimeDataCall1>(taken[1]);
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
      CuteQTableWidgetMimeDataCall2 call = reinterpret_cast<CuteQTableWidgetMimeDataCall2>(taken[2]);
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
      CuteQTableWidgetMimeDataCall3 call = reinterpret_cast<CuteQTableWidgetMimeDataCall3>(taken[3]);
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
      CuteQTableWidgetMimeDataCall4 call = reinterpret_cast<CuteQTableWidgetMimeDataCall4>(taken[4]);
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
      CuteQTableWidgetMimeDataCall5 call = reinterpret_cast<CuteQTableWidgetMimeDataCall5>(taken[5]);
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
      CuteQTableWidgetMimeDataCall6 call = reinterpret_cast<CuteQTableWidgetMimeDataCall6>(taken[6]);
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
      CuteQTableWidgetMimeDataCall7 call = reinterpret_cast<CuteQTableWidgetMimeDataCall7>(taken[7]);
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
      CuteQTableWidgetMimeDataCall8 call = reinterpret_cast<CuteQTableWidgetMimeDataCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTableWidgetMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QTableWidgetMimeData10metaObjectEv(
    const QTableWidgetMimeData *self) {
  return self->metaObject();
}

//  void *QTableWidgetMimeData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QTableWidgetMimeData11qt_metacastEPKc(
    QTableWidgetMimeData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTableWidgetMimeData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTableWidgetMimeData11qt_metacallEN11QMetaObject4CallEiPPv(
    QTableWidgetMimeData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  a Python function taken by a CuteQTableWidgetMimeData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableWidgetMimeData(
    QTableWidgetMimeData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTableWidgetMimeData *>(self)->take(key, call);
}

#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(tablewidget)
