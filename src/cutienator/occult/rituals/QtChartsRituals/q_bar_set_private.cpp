//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qbarset_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qbarset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBarSetPrivate that Python can take functions over in. Every QBarSetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarSetPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarSetPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarSetPrivate : public QBarSetPrivate {
public:
  using QBarSetPrivate::QBarSetPrivate;
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
      CuteQBarSetPrivateCall0 call = reinterpret_cast<CuteQBarSetPrivateCall0>(taken[0]);
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
      CuteQBarSetPrivateCall1 call = reinterpret_cast<CuteQBarSetPrivateCall1>(taken[1]);
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
      CuteQBarSetPrivateCall2 call = reinterpret_cast<CuteQBarSetPrivateCall2>(taken[2]);
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
      CuteQBarSetPrivateCall3 call = reinterpret_cast<CuteQBarSetPrivateCall3>(taken[3]);
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
      CuteQBarSetPrivateCall4 call = reinterpret_cast<CuteQBarSetPrivateCall4>(taken[4]);
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
      CuteQBarSetPrivateCall5 call = reinterpret_cast<CuteQBarSetPrivateCall5>(taken[5]);
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
      CuteQBarSetPrivateCall6 call = reinterpret_cast<CuteQBarSetPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarSetPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QBarSetPrivate10metaObjectEv(
    const QBarSetPrivate *self) {
  return self->metaObject();
}

//  void *QBarSetPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QBarSetPrivate11qt_metacastEPKc(
    QBarSetPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarSetPrivate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QBarSetPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarSetPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBarSetPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBarSetPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarSetPrivate::tr(s, c, n));
}

//  QBarSetPrivate::QBarSetPrivate(const QString label, QBarSet *parent)
extern "C" Q_DECL_EXPORT
QBarSetPrivate *ritual_ZN14QBarSetPrivateC1E7QStringP7QBarSet(
    const QString *label,
    QBarSet *parent) {
  return new CuteQBarSetPrivate(*label, parent);
}

//  QBarSetPrivate::~QBarSetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivateD1Ev(QBarSetPrivate *self) {
  delete self;
}

//  void QBarSetPrivate::append(QPointF value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6appendE7QPointF(
    QBarSetPrivate *self,
    const QPointF *value) {
  self->append(*value);
}

//  void QBarSetPrivate::append(const QList<QPointF> &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6appendERK5QListI7QPointFE(
    QBarSetPrivate *self,
    const QList<QPointF> *values) {
  self->append(*values);
}

//  void QBarSetPrivate::append(const QList<qreal> &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6appendERK5QListIdE(
    QBarSetPrivate *self,
    const QList<qreal> *values) {
  self->append(*values);
}

//  void QBarSetPrivate::insert(const int index, const qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6insertEid(
    QBarSetPrivate *self,
    int index,
    qreal value) {
  self->insert(index, value);
}

//  void QBarSetPrivate::insert(const int index, const QPointF value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6insertEi7QPointF(
    QBarSetPrivate *self,
    int index,
    const QPointF *value) {
  self->insert(index, *value);
}

//  int QBarSetPrivate::remove(const int index, const int count)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QBarSetPrivate6removeEii(
    QBarSetPrivate *self,
    int index,
    int count) {
  return self->remove(index, count);
}

//  void QBarSetPrivate::replace(const int index, const qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate7replaceEid(
    QBarSetPrivate *self,
    int index,
    qreal value) {
  self->replace(index, value);
}

//  qreal QBarSetPrivate::pos(const int index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QBarSetPrivate3posEi(QBarSetPrivate *self, int index) {
  return self->pos(index);
}

//  qreal QBarSetPrivate::value(const int index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QBarSetPrivate5valueEi(QBarSetPrivate *self, int index) {
  return self->value(index);
}

//  void QBarSetPrivate::setVisualsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate15setVisualsDirtyEb(
    QBarSetPrivate *self,
    bool dirty) {
  self->setVisualsDirty(dirty);
}

//  bool QBarSetPrivate::visualsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBarSetPrivate12visualsDirtyEv(const QBarSetPrivate *self) {
  return self->visualsDirty();
}

//  void QBarSetPrivate::setLabelsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate14setLabelsDirtyEb(
    QBarSetPrivate *self,
    bool dirty) {
  self->setLabelsDirty(dirty);
}

//  bool QBarSetPrivate::labelsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBarSetPrivate11labelsDirtyEv(const QBarSetPrivate *self) {
  return self->labelsDirty();
}

//  void QBarSetPrivate::setBarSelected(int index, bool selected, bool
//      &callSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate14setBarSelectedEibRb(
    QBarSetPrivate *self,
    int index,
    bool selected,
    bool *callSignal) {
  self->setBarSelected(index, selected, *callSignal);
}

//  bool QBarSetPrivate::isBarSelected(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBarSetPrivate13isBarSelectedEi(
    const QBarSetPrivate *self,
    int index) {
  return self->isBarSelected(index);
}

//  void QBarSetPrivate::updatedBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate11updatedBarsEv(QBarSetPrivate *self) {
  self->updatedBars();
}

//  void QBarSetPrivate::valueChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate12valueChangedEi(
    QBarSetPrivate *self,
    int index) {
  self->valueChanged(index);
}

//  void QBarSetPrivate::valueAdded(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate10valueAddedEii(
    QBarSetPrivate *self,
    int index,
    int count) {
  self->valueAdded(index, count);
}

//  void QBarSetPrivate::valueRemoved(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate12valueRemovedEii(
    QBarSetPrivate *self,
    int index,
    int count) {
  self->valueRemoved(index, count);
}

//  a Python function taken by a CuteQBarSetPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarSetPrivate(
    QBarSetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarSetPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_bar_chart)
