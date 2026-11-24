//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlrolesorter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlrolesorter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qcompare.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlRoleSorter that Python can take functions over in. Every QQmlRoleSorter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPartialOrdering * (*CuteQQmlRoleSorterCall0)(const void *, const QModelIndex *, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlRoleSorterCall1)(const void *, const QQmlSortFilterProxyModel *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlRoleSorterCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlRoleSorterCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleSorterCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleSorterCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleSorterCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleSorterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleSorterCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlRoleSorter : public QQmlRoleSorter {
public:
  using QQmlRoleSorter::QQmlRoleSorter;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQmlSorterBase7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlSorterBase6updateEPK24QQmlSortFilterProxyModel")) {
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

  //  QPartialOrdering QQmlRoleSorter::compare(const QModelIndex
  //      &sourceLeft, const QModelIndex &sourceRight, const
  //      QQmlSortFilterProxyModel *proxyModel) const
  QPartialOrdering compare(
      const QModelIndex &sourceLeft,
      const QModelIndex &sourceRight,
      const QQmlSortFilterProxyModel *proxyModel) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlRoleSorterCall0 call = reinterpret_cast<CuteQQmlRoleSorterCall0>(taken[0]);
      const QPartialOrdering * given = call(this, &sourceLeft, &sourceRight, proxyModel, &handled);
      if (handled && given) return *given;
    }
    return QQmlRoleSorter::compare(sourceLeft, sourceRight, proxyModel);
  }

  //  void QQmlRoleSorter::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlRoleSorterCall1 call = reinterpret_cast<CuteQQmlRoleSorterCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlRoleSorter::update(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlRoleSorterCall2 call = reinterpret_cast<CuteQQmlRoleSorterCall2>(taken[2]);
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
      CuteQQmlRoleSorterCall3 call = reinterpret_cast<CuteQQmlRoleSorterCall3>(taken[3]);
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
      CuteQQmlRoleSorterCall4 call = reinterpret_cast<CuteQQmlRoleSorterCall4>(taken[4]);
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
      CuteQQmlRoleSorterCall5 call = reinterpret_cast<CuteQQmlRoleSorterCall5>(taken[5]);
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
      CuteQQmlRoleSorterCall6 call = reinterpret_cast<CuteQQmlRoleSorterCall6>(taken[6]);
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
      CuteQQmlRoleSorterCall7 call = reinterpret_cast<CuteQQmlRoleSorterCall7>(taken[7]);
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
      CuteQQmlRoleSorterCall8 call = reinterpret_cast<CuteQQmlRoleSorterCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlRoleSorter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlRoleSorter10metaObjectEv(
    const QQmlRoleSorter *self) {
  return self->metaObject();
}

//  QString QQmlRoleSorter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlRoleSorter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlRoleSorter::tr(s, c, n));
}

//  QQmlRoleSorter::QQmlRoleSorter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlRoleSorter *ritual_ZN14QQmlRoleSorterC1EP7QObject(QObject *parent) {
  return new CuteQQmlRoleSorter(parent);
}

//  QQmlRoleSorter::QQmlRoleSorter(QQmlSorterBasePrivate *priv, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlRoleSorter *ritual_ZN14QQmlRoleSorterC1EP21QQmlSorterBasePrivateP7QObject(
    QQmlSorterBasePrivate *priv,
    QObject *parent) {
  return new CuteQQmlRoleSorter(priv, parent);
}

//  QQmlRoleSorter::~QQmlRoleSorter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleSorterD1Ev(QQmlRoleSorter *self) {
  delete self;
}

//  const QString &QQmlRoleSorter::roleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlRoleSorter8roleNameEv(const QQmlRoleSorter *self) {
  return new QString(self->roleName());
}

//  void QQmlRoleSorter::setRoleName(const QString &roleName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleSorter11setRoleNameERK7QString(
    QQmlRoleSorter *self,
    const QString *roleName) {
  self->setRoleName(*roleName);
}

//  QPartialOrdering QQmlRoleSorter::compare(const QModelIndex &sourceLeft,
//      const QModelIndex &sourceRight, const QQmlSortFilterProxyModel
//      *proxyModel) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZNK14QQmlRoleSorter7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlRoleSorter *self,
    const QModelIndex *sourceLeft,
    const QModelIndex *sourceRight,
    const QQmlSortFilterProxyModel *proxyModel) {
  return new QPartialOrdering(
      self->compare(
          *sourceLeft,
          *sourceRight,
          proxyModel));
}

//  void QQmlRoleSorter::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleSorter6updateEPK24QQmlSortFilterProxyModel(
    QQmlRoleSorter *self,
    const QQmlSortFilterProxyModel *a0) {
  self->update(a0);
}

//  QQmlRoleSorterPrivate *QQmlRoleSorter::d_func()
extern "C" Q_DECL_EXPORT
QQmlRoleSorterPrivate *ritual_ZN14QQmlRoleSorter6d_funcEv(
    QQmlRoleSorter *self) {
  return self->d_func();
}

//  const QQmlRoleSorterPrivate *QQmlRoleSorter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlRoleSorterPrivate *ritual_ZNK14QQmlRoleSorter6d_funcEv(
    const QQmlRoleSorter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlRoleSorter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlRoleSorter(
    QQmlRoleSorter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlRoleSorter *>(self)->take(key, call);
}

//  QPartialOrdering QQmlRoleSorter::compare(const QModelIndex &sourceLeft,
//      const QModelIndex &sourceRight, const QQmlSortFilterProxyModel
//      *proxyModel) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_own_ZNK14QQmlRoleSorter7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlRoleSorter *self,
    const QModelIndex *sourceLeft,
    const QModelIndex *sourceRight,
    const QQmlSortFilterProxyModel *proxyModel) {
  return new QPartialOrdering(
      self->QQmlRoleSorter::compare(
          *sourceLeft,
          *sourceRight,
          proxyModel));
}

//  void QQmlRoleSorter::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlRoleSorter6updateEPK24QQmlSortFilterProxyModel(
    QQmlRoleSorter *self,
    const QQmlSortFilterProxyModel *a0) {
  self->QQmlRoleSorter::update(a0);
}
