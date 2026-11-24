//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfunctionsorter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlfunctionsorter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qcompare.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlFunctionSorter that Python can take functions over in. Every QQmlFunctionSorter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPartialOrdering * (*CuteQQmlFunctionSorterCall0)(const void *, const QModelIndex *, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlFunctionSorterCall1)(const void *, int *);
typedef void (*CuteQQmlFunctionSorterCall2)(const void *, int *);
typedef void (*CuteQQmlFunctionSorterCall3)(const void *, const QQmlSortFilterProxyModel *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlFunctionSorterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlFunctionSorterCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionSorterCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionSorterCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionSorterCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionSorterCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionSorterCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlFunctionSorter : public QQmlFunctionSorter {
public:
  using QQmlFunctionSorter::QQmlFunctionSorter;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQmlSorterBase7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlSorterBase6updateEPK24QQmlSortFilterProxyModel")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPartialOrdering QQmlFunctionSorter::compare(const QModelIndex &a0,
  //      const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
  QPartialOrdering compare(
      const QModelIndex &a0,
      const QModelIndex &a1,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall0 call = reinterpret_cast<CuteQQmlFunctionSorterCall0>(taken[0]);
      const QPartialOrdering * given = call(this, &a0, &a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QQmlFunctionSorter::compare(a0, a1, a2);
  }

  //  void QQmlFunctionSorter::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall1 call = reinterpret_cast<CuteQQmlFunctionSorterCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlFunctionSorter::classBegin();
  }

  //  void QQmlFunctionSorter::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall2 call = reinterpret_cast<CuteQQmlFunctionSorterCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlFunctionSorter::componentComplete();
  }

  //  void QQmlSorterBase::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall3 call = reinterpret_cast<CuteQQmlFunctionSorterCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlSorterBase::update(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall4 call = reinterpret_cast<CuteQQmlFunctionSorterCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall5 call = reinterpret_cast<CuteQQmlFunctionSorterCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall6 call = reinterpret_cast<CuteQQmlFunctionSorterCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall7 call = reinterpret_cast<CuteQQmlFunctionSorterCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall8 call = reinterpret_cast<CuteQQmlFunctionSorterCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall9 call = reinterpret_cast<CuteQQmlFunctionSorterCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlFunctionSorterCall10 call = reinterpret_cast<CuteQQmlFunctionSorterCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlFunctionSorter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQmlFunctionSorter10metaObjectEv(
    const QQmlFunctionSorter *self) {
  return self->metaObject();
}

//  QString QQmlFunctionSorter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlFunctionSorter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlFunctionSorter::tr(s, c, n));
}

//  QQmlFunctionSorter::QQmlFunctionSorter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlFunctionSorter *ritual_ZN18QQmlFunctionSorterC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlFunctionSorter(parent);
}

//  QQmlFunctionSorter::~QQmlFunctionSorter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionSorterD1Ev(QQmlFunctionSorter *self) {
  delete self;
}

//  QPartialOrdering QQmlFunctionSorter::compare(const QModelIndex &a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZNK18QQmlFunctionSorter7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlFunctionSorter *self,
    const QModelIndex *a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return new QPartialOrdering(self->compare(*a0, *a1, a2));
}

//  void QQmlFunctionSorter::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionSorter10classBeginEv(QQmlFunctionSorter *self) {
  self->classBegin();
}

//  void QQmlFunctionSorter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionSorter17componentCompleteEv(
    QQmlFunctionSorter *self) {
  self->componentComplete();
}

//  QQmlFunctionSorterPrivate *QQmlFunctionSorter::d_func()
extern "C" Q_DECL_EXPORT
QQmlFunctionSorterPrivate *ritual_ZN18QQmlFunctionSorter6d_funcEv(
    QQmlFunctionSorter *self) {
  return self->d_func();
}

//  const QQmlFunctionSorterPrivate *QQmlFunctionSorter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlFunctionSorterPrivate *ritual_ZNK18QQmlFunctionSorter6d_funcEv(
    const QQmlFunctionSorter *self) {
  return self->d_func();
}

//  QQmlFunctionSorter as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlFunctionSorter_QQmlParserStatus(
    QQmlFunctionSorter *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlFunctionSorter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlFunctionSorter(
    QQmlFunctionSorter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlFunctionSorter *>(self)->take(key, call);
}

//  QPartialOrdering QQmlFunctionSorter::compare(const QModelIndex &a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_own_ZNK18QQmlFunctionSorter7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlFunctionSorter *self,
    const QModelIndex *a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return new QPartialOrdering(
      self->QQmlFunctionSorter::compare(
          *a0,
          *a1,
          a2));
}

//  void QQmlFunctionSorter::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlFunctionSorter10classBeginEv(
    QQmlFunctionSorter *self) {
  self->QQmlFunctionSorter::classBegin();
}

//  void QQmlFunctionSorter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlFunctionSorter17componentCompleteEv(
    QQmlFunctionSorter *self) {
  self->QQmlFunctionSorter::componentComplete();
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
