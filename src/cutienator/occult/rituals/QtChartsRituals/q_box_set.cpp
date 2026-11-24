//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qboxset.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qboxset.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBoxSet that Python can take functions over in. Every QBoxSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxSetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxSetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxSet : public QBoxSet {
public:
  using QBoxSet::QBoxSet;
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
      CuteQBoxSetCall0 call = reinterpret_cast<CuteQBoxSetCall0>(taken[0]);
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
      CuteQBoxSetCall1 call = reinterpret_cast<CuteQBoxSetCall1>(taken[1]);
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
      CuteQBoxSetCall2 call = reinterpret_cast<CuteQBoxSetCall2>(taken[2]);
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
      CuteQBoxSetCall3 call = reinterpret_cast<CuteQBoxSetCall3>(taken[3]);
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
      CuteQBoxSetCall4 call = reinterpret_cast<CuteQBoxSetCall4>(taken[4]);
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
      CuteQBoxSetCall5 call = reinterpret_cast<CuteQBoxSetCall5>(taken[5]);
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
      CuteQBoxSetCall6 call = reinterpret_cast<CuteQBoxSetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QBoxSet10metaObjectEv(const QBoxSet *self) {
  return self->metaObject();
}

//  QString QBoxSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QBoxSet2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QBoxSet::tr(s, c, n));
}

//  QBoxSet::QBoxSet(const QString label, QObject *parent)
extern "C" Q_DECL_EXPORT
QBoxSet *ritual_ZN7QBoxSetC1E7QStringP7QObject(
    const QString *label,
    QObject *parent) {
  return new CuteQBoxSet(*label, parent);
}

//  QBoxSet::QBoxSet(const qreal le, const qreal lq, const qreal m, const
//      qreal uq, const qreal ue, const QString label, QObject *parent)
extern "C" Q_DECL_EXPORT
QBoxSet *ritual_ZN7QBoxSetC1Eddddd7QStringP7QObject(
    qreal le,
    qreal lq,
    qreal m,
    qreal uq,
    qreal ue,
    const QString *label,
    QObject *parent) {
  return new CuteQBoxSet(le, lq, m, uq, ue, *label, parent);
}

//  QBoxSet::~QBoxSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSetD1Ev(QBoxSet *self) {
  delete self;
}

//  void QBoxSet::append(const qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSet6appendEd(QBoxSet *self, qreal value) {
  self->append(value);
}

//  void QBoxSet::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSet5clearEv(QBoxSet *self) {
  self->clear();
}

//  void QBoxSet::setLabel(const QString label)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSet8setLabelE7QString(
    QBoxSet *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QString QBoxSet::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QBoxSet5labelEv(const QBoxSet *self) {
  return new QString(self->label());
}

//  void QBoxSet::setValue(const int index, const qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSet8setValueEid(QBoxSet *self, int index, qreal value) {
  self->setValue(index, value);
}

//  qreal QBoxSet::at(const int index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBoxSet2atEi(const QBoxSet *self, int index) {
  return self->at(index);
}

//  qreal QBoxSet::operator[](const int index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBoxSetixEi(const QBoxSet *self, int index) {
  return self->operator[](index);
}

//  int QBoxSet::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QBoxSet5countEv(const QBoxSet *self) {
  return self->count();
}

//  void QBoxSet::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSet6setPenERK4QPen(QBoxSet *self, const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QBoxSet::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK7QBoxSet3penEv(const QBoxSet *self) {
  return new QPen(self->pen());
}

//  void QBoxSet::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBoxSet8setBrushERK6QBrush(
    QBoxSet *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QBoxSet::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK7QBoxSet5brushEv(const QBoxSet *self) {
  return new QBrush(self->brush());
}

//  a Python function taken by a CuteQBoxSet, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxSet(QBoxSet *self, const char *key, void *call) {
  return static_cast<CuteQBoxSet *>(self)->take(key, call);
}

//  QList<QBoxSet *>::QList()
extern "C" Q_DECL_EXPORT
QList<QBoxSet *> *ritual_list_make_QBoxSet_ptr() {
  return new QList<QBoxSet *>();
}

//  void QList<QBoxSet *>::append(const QBoxSet * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBoxSet_ptr(QList<QBoxSet *> *self, QBoxSet *element) {
  self->append(element);
}

//  qsizetype QList<QBoxSet *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBoxSet_ptr(const QList<QBoxSet *> *self) {
  return self->size();
}

//  const QBoxSet * &QList<QBoxSet *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QBoxSet *ritual_list_at_QBoxSet_ptr(
    const QList<QBoxSet *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QBoxSet *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBoxSet_ptr(QList<QBoxSet *> *self) {
  delete self;
}
