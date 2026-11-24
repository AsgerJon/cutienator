//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qitemmodelscatterdataproxy.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qitemmodelscatterdataproxy.h>
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QItemModelScatterDataProxy that Python can take functions over in. Every QItemModelScatterDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelScatterDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelScatterDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemModelScatterDataProxy : public QItemModelScatterDataProxy {
public:
  using QItemModelScatterDataProxy::QItemModelScatterDataProxy;
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
      CuteQItemModelScatterDataProxyCall0 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall0>(taken[0]);
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
      CuteQItemModelScatterDataProxyCall1 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall1>(taken[1]);
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
      CuteQItemModelScatterDataProxyCall2 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall2>(taken[2]);
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
      CuteQItemModelScatterDataProxyCall3 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall3>(taken[3]);
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
      CuteQItemModelScatterDataProxyCall4 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall4>(taken[4]);
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
      CuteQItemModelScatterDataProxyCall5 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall5>(taken[5]);
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
      CuteQItemModelScatterDataProxyCall6 call = reinterpret_cast<CuteQItemModelScatterDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QItemModelScatterDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QItemModelScatterDataProxy10metaObjectEv(
    const QItemModelScatterDataProxy *self) {
  return self->metaObject();
}

//  QString QItemModelScatterDataProxy::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QItemModelScatterDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemModelScatterDataProxy::tr(s, c, n));
}

//  QItemModelScatterDataProxyPrivate *QItemModelScatterDataProxy::d_func()
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxyPrivate *ritual_ZN26QItemModelScatterDataProxy6d_funcEv(
    QItemModelScatterDataProxy *self) {
  return self->d_func();
}

//  const QItemModelScatterDataProxyPrivate
//      *QItemModelScatterDataProxy::d_func() const
extern "C" Q_DECL_EXPORT
const QItemModelScatterDataProxyPrivate *ritual_ZNK26QItemModelScatterDataProxy6d_funcEv(
    const QItemModelScatterDataProxy *self) {
  return self->d_func();
}

//  QItemModelScatterDataProxy::QItemModelScatterDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxy *ritual_ZN26QItemModelScatterDataProxyC1EP7QObject(
    QObject *parent) {
  return new CuteQItemModelScatterDataProxy(parent);
}

//  QItemModelScatterDataProxy::QItemModelScatterDataProxy(QAbstractItemModel
//      *itemModel, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxy *ritual_ZN26QItemModelScatterDataProxyC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *itemModel,
    QObject *parent) {
  return new CuteQItemModelScatterDataProxy(itemModel, parent);
}

//  QItemModelScatterDataProxy::QItemModelScatterDataProxy(QAbstractItemModel
//      *itemModel, const QString &xPosRole, const QString &yPosRole, const
//      QString &zPosRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxy *ritual_ZN26QItemModelScatterDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    QObject *parent) {
  return new CuteQItemModelScatterDataProxy(
      itemModel,
      *xPosRole,
      *yPosRole,
      *zPosRole,
      parent);
}

//  QItemModelScatterDataProxy::QItemModelScatterDataProxy(QAbstractItemModel
//      *itemModel, const QString &xPosRole, const QString &yPosRole, const
//      QString &zPosRole, const QString &rotationRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxy *ritual_ZN26QItemModelScatterDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_S4_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    const QString *rotationRole,
    QObject *parent) {
  return new CuteQItemModelScatterDataProxy(
      itemModel,
      *xPosRole,
      *yPosRole,
      *zPosRole,
      *rotationRole,
      parent);
}

//  QItemModelScatterDataProxy::~QItemModelScatterDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxyD1Ev(
    QItemModelScatterDataProxy *self) {
  delete self;
}

//  void QItemModelScatterDataProxy::setItemModel(QAbstractItemModel
//      *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy12setItemModelEP18QAbstractItemModel(
    QItemModelScatterDataProxy *self,
    QAbstractItemModel *itemModel) {
  self->setItemModel(itemModel);
}

//  QAbstractItemModel *QItemModelScatterDataProxy::itemModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK26QItemModelScatterDataProxy9itemModelEv(
    const QItemModelScatterDataProxy *self) {
  return self->itemModel();
}

//  void QItemModelScatterDataProxy::setXPosRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy11setXPosRoleERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *role) {
  self->setXPosRole(*role);
}

//  QString QItemModelScatterDataProxy::xPosRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy8xPosRoleEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->xPosRole());
}

//  void QItemModelScatterDataProxy::setYPosRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy11setYPosRoleERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *role) {
  self->setYPosRole(*role);
}

//  QString QItemModelScatterDataProxy::yPosRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy8yPosRoleEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->yPosRole());
}

//  void QItemModelScatterDataProxy::setZPosRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy11setZPosRoleERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *role) {
  self->setZPosRole(*role);
}

//  QString QItemModelScatterDataProxy::zPosRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy8zPosRoleEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->zPosRole());
}

//  void QItemModelScatterDataProxy::setRotationRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy15setRotationRoleERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *role) {
  self->setRotationRole(*role);
}

//  QString QItemModelScatterDataProxy::rotationRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy12rotationRoleEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->rotationRole());
}

//  void QItemModelScatterDataProxy::setScaleRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy12setScaleRoleERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *role) {
  self->setScaleRole(*role);
}

//  QString QItemModelScatterDataProxy::scaleRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy9scaleRoleEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->scaleRole());
}

//  void QItemModelScatterDataProxy::remap(const QString &xPosRole, const
//      QString &yPosRole, const QString &zPosRole, const QString
//      &rotationRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy5remapERK7QStringS2_S2_S2_(
    QItemModelScatterDataProxy *self,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    const QString *rotationRole) {
  self->remap(*xPosRole, *yPosRole, *zPosRole, *rotationRole);
}

//  void QItemModelScatterDataProxy::remap(const QString &xPosRole, const
//      QString &yPosRole, const QString &zPosRole, const QString
//      &rotationRole, const QString &scaleRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy5remapERK7QStringS2_S2_S2_S2_(
    QItemModelScatterDataProxy *self,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    const QString *rotationRole,
    const QString *scaleRole) {
  self->remap(*xPosRole, *yPosRole, *zPosRole, *rotationRole, *scaleRole);
}

//  void QItemModelScatterDataProxy::setXPosRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy18setXPosRolePatternERK18QRegularExpression(
    QItemModelScatterDataProxy *self,
    const QRegularExpression *pattern) {
  self->setXPosRolePattern(*pattern);
}

//  QRegularExpression QItemModelScatterDataProxy::xPosRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelScatterDataProxy15xPosRolePatternEv(
    const QItemModelScatterDataProxy *self) {
  return new QRegularExpression(self->xPosRolePattern());
}

//  void QItemModelScatterDataProxy::setYPosRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy18setYPosRolePatternERK18QRegularExpression(
    QItemModelScatterDataProxy *self,
    const QRegularExpression *pattern) {
  self->setYPosRolePattern(*pattern);
}

//  QRegularExpression QItemModelScatterDataProxy::yPosRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelScatterDataProxy15yPosRolePatternEv(
    const QItemModelScatterDataProxy *self) {
  return new QRegularExpression(self->yPosRolePattern());
}

//  void QItemModelScatterDataProxy::setZPosRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy18setZPosRolePatternERK18QRegularExpression(
    QItemModelScatterDataProxy *self,
    const QRegularExpression *pattern) {
  self->setZPosRolePattern(*pattern);
}

//  QRegularExpression QItemModelScatterDataProxy::zPosRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelScatterDataProxy15zPosRolePatternEv(
    const QItemModelScatterDataProxy *self) {
  return new QRegularExpression(self->zPosRolePattern());
}

//  void QItemModelScatterDataProxy::setRotationRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy22setRotationRolePatternERK18QRegularExpression(
    QItemModelScatterDataProxy *self,
    const QRegularExpression *pattern) {
  self->setRotationRolePattern(*pattern);
}

//  QRegularExpression QItemModelScatterDataProxy::rotationRolePattern()
//      const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelScatterDataProxy19rotationRolePatternEv(
    const QItemModelScatterDataProxy *self) {
  return new QRegularExpression(self->rotationRolePattern());
}

//  void QItemModelScatterDataProxy::setScaleRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy19setScaleRolePatternERK18QRegularExpression(
    QItemModelScatterDataProxy *self,
    const QRegularExpression *pattern) {
  self->setScaleRolePattern(*pattern);
}

//  QRegularExpression QItemModelScatterDataProxy::scaleRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelScatterDataProxy16scaleRolePatternEv(
    const QItemModelScatterDataProxy *self) {
  return new QRegularExpression(self->scaleRolePattern());
}

//  void QItemModelScatterDataProxy::setXPosRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy18setXPosRoleReplaceERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *replace) {
  self->setXPosRoleReplace(*replace);
}

//  QString QItemModelScatterDataProxy::xPosRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy15xPosRoleReplaceEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->xPosRoleReplace());
}

//  void QItemModelScatterDataProxy::setYPosRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy18setYPosRoleReplaceERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *replace) {
  self->setYPosRoleReplace(*replace);
}

//  QString QItemModelScatterDataProxy::yPosRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy15yPosRoleReplaceEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->yPosRoleReplace());
}

//  void QItemModelScatterDataProxy::setZPosRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy18setZPosRoleReplaceERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *replace) {
  self->setZPosRoleReplace(*replace);
}

//  QString QItemModelScatterDataProxy::zPosRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy15zPosRoleReplaceEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->zPosRoleReplace());
}

//  void QItemModelScatterDataProxy::setRotationRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy22setRotationRoleReplaceERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *replace) {
  self->setRotationRoleReplace(*replace);
}

//  QString QItemModelScatterDataProxy::rotationRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy19rotationRoleReplaceEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->rotationRoleReplace());
}

//  void QItemModelScatterDataProxy::setScaleRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelScatterDataProxy19setScaleRoleReplaceERK7QString(
    QItemModelScatterDataProxy *self,
    const QString *replace) {
  self->setScaleRoleReplace(*replace);
}

//  QString QItemModelScatterDataProxy::scaleRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelScatterDataProxy16scaleRoleReplaceEv(
    const QItemModelScatterDataProxy *self) {
  return new QString(self->scaleRoleReplace());
}

//  a Python function taken by a CuteQItemModelScatterDataProxy, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelScatterDataProxy(
    QItemModelScatterDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelScatterDataProxy *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
