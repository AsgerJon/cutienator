//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qitemmodelbardataproxy.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qitemmodelbardataproxy.h>
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QItemModelBarDataProxy that Python can take functions over in. Every QItemModelBarDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelBarDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelBarDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelBarDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelBarDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelBarDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelBarDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelBarDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemModelBarDataProxy : public QItemModelBarDataProxy {
public:
  using QItemModelBarDataProxy::QItemModelBarDataProxy;
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
      CuteQItemModelBarDataProxyCall0 call = reinterpret_cast<CuteQItemModelBarDataProxyCall0>(taken[0]);
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
      CuteQItemModelBarDataProxyCall1 call = reinterpret_cast<CuteQItemModelBarDataProxyCall1>(taken[1]);
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
      CuteQItemModelBarDataProxyCall2 call = reinterpret_cast<CuteQItemModelBarDataProxyCall2>(taken[2]);
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
      CuteQItemModelBarDataProxyCall3 call = reinterpret_cast<CuteQItemModelBarDataProxyCall3>(taken[3]);
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
      CuteQItemModelBarDataProxyCall4 call = reinterpret_cast<CuteQItemModelBarDataProxyCall4>(taken[4]);
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
      CuteQItemModelBarDataProxyCall5 call = reinterpret_cast<CuteQItemModelBarDataProxyCall5>(taken[5]);
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
      CuteQItemModelBarDataProxyCall6 call = reinterpret_cast<CuteQItemModelBarDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QItemModelBarDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QItemModelBarDataProxy10metaObjectEv(
    const QItemModelBarDataProxy *self) {
  return self->metaObject();
}

//  QString QItemModelBarDataProxy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QItemModelBarDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemModelBarDataProxy::tr(s, c, n));
}

//  QItemModelBarDataProxyPrivate *QItemModelBarDataProxy::d_func()
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxyPrivate *ritual_ZN22QItemModelBarDataProxy6d_funcEv(
    QItemModelBarDataProxy *self) {
  return self->d_func();
}

//  const QItemModelBarDataProxyPrivate *QItemModelBarDataProxy::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QItemModelBarDataProxyPrivate *ritual_ZNK22QItemModelBarDataProxy6d_funcEv(
    const QItemModelBarDataProxy *self) {
  return self->d_func();
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP7QObject(
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(parent);
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
//      *itemModel, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *itemModel,
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(itemModel, parent);
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
//      *itemModel, const QString &valueRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStringP7QObject(
    QAbstractItemModel *itemModel,
    const QString *valueRole,
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(itemModel, *valueRole, parent);
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &valueRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *valueRole,
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *valueRole,
      parent);
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &valueRole, const QString &rotationRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_S4_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *valueRole,
    const QString *rotationRole,
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *valueRole,
      *rotationRole,
      parent);
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &valueRole, const QStringList &rowCategories, const
//      QStringList &columnCategories, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_RK5QListIS2_ES8_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *valueRole,
    const QList<QString> *rowCategories,
    const QList<QString> *columnCategories,
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *valueRole,
      *rowCategories,
      *columnCategories,
      parent);
}

//  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &valueRole, const QString &rotationRole, const QStringList
//      &rowCategories, const QStringList &columnCategories, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_S4_RK5QListIS2_ES8_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *valueRole,
    const QString *rotationRole,
    const QList<QString> *rowCategories,
    const QList<QString> *columnCategories,
    QObject *parent) {
  return new CuteQItemModelBarDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *valueRole,
      *rotationRole,
      *rowCategories,
      *columnCategories,
      parent);
}

//  QItemModelBarDataProxy::~QItemModelBarDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxyD1Ev(QItemModelBarDataProxy *self) {
  delete self;
}

//  void QItemModelBarDataProxy::setItemModel(QAbstractItemModel *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy12setItemModelEP18QAbstractItemModel(
    QItemModelBarDataProxy *self,
    QAbstractItemModel *itemModel) {
  self->setItemModel(itemModel);
}

//  QAbstractItemModel *QItemModelBarDataProxy::itemModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK22QItemModelBarDataProxy9itemModelEv(
    const QItemModelBarDataProxy *self) {
  return self->itemModel();
}

//  void QItemModelBarDataProxy::setRowRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy10setRowRoleERK7QString(
    QItemModelBarDataProxy *self,
    const QString *role) {
  self->setRowRole(*role);
}

//  QString QItemModelBarDataProxy::rowRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy7rowRoleEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->rowRole());
}

//  void QItemModelBarDataProxy::setColumnRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy13setColumnRoleERK7QString(
    QItemModelBarDataProxy *self,
    const QString *role) {
  self->setColumnRole(*role);
}

//  QString QItemModelBarDataProxy::columnRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy10columnRoleEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->columnRole());
}

//  void QItemModelBarDataProxy::setValueRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy12setValueRoleERK7QString(
    QItemModelBarDataProxy *self,
    const QString *role) {
  self->setValueRole(*role);
}

//  QString QItemModelBarDataProxy::valueRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy9valueRoleEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->valueRole());
}

//  void QItemModelBarDataProxy::setRotationRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy15setRotationRoleERK7QString(
    QItemModelBarDataProxy *self,
    const QString *role) {
  self->setRotationRole(*role);
}

//  QString QItemModelBarDataProxy::rotationRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy12rotationRoleEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->rotationRole());
}

//  void QItemModelBarDataProxy::setRowCategories(const QStringList
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy16setRowCategoriesERK5QListI7QStringE(
    QItemModelBarDataProxy *self,
    const QList<QString> *categories) {
  self->setRowCategories(*categories);
}

//  QStringList QItemModelBarDataProxy::rowCategories() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QItemModelBarDataProxy13rowCategoriesEv(
    const QItemModelBarDataProxy *self) {
  return new QList<QString>(self->rowCategories());
}

//  void QItemModelBarDataProxy::setColumnCategories(const QStringList
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy19setColumnCategoriesERK5QListI7QStringE(
    QItemModelBarDataProxy *self,
    const QList<QString> *categories) {
  self->setColumnCategories(*categories);
}

//  QStringList QItemModelBarDataProxy::columnCategories() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QItemModelBarDataProxy16columnCategoriesEv(
    const QItemModelBarDataProxy *self) {
  return new QList<QString>(self->columnCategories());
}

//  void QItemModelBarDataProxy::setUseModelCategories(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy21setUseModelCategoriesEb(
    QItemModelBarDataProxy *self,
    bool enable) {
  self->setUseModelCategories(enable);
}

//  bool QItemModelBarDataProxy::useModelCategories() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QItemModelBarDataProxy18useModelCategoriesEv(
    const QItemModelBarDataProxy *self) {
  return self->useModelCategories();
}

//  void QItemModelBarDataProxy::setAutoRowCategories(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy20setAutoRowCategoriesEb(
    QItemModelBarDataProxy *self,
    bool enable) {
  self->setAutoRowCategories(enable);
}

//  bool QItemModelBarDataProxy::autoRowCategories() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QItemModelBarDataProxy17autoRowCategoriesEv(
    const QItemModelBarDataProxy *self) {
  return self->autoRowCategories();
}

//  void QItemModelBarDataProxy::setAutoColumnCategories(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy23setAutoColumnCategoriesEb(
    QItemModelBarDataProxy *self,
    bool enable) {
  self->setAutoColumnCategories(enable);
}

//  bool QItemModelBarDataProxy::autoColumnCategories() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QItemModelBarDataProxy20autoColumnCategoriesEv(
    const QItemModelBarDataProxy *self) {
  return self->autoColumnCategories();
}

//  void QItemModelBarDataProxy::remap(const QString &rowRole, const QString
//      &columnRole, const QString &valueRole, const QString &rotationRole,
//      const QStringList &rowCategories, const QStringList
//      &columnCategories)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy5remapERK7QStringS2_S2_S2_RK5QListIS0_ES6_(
    QItemModelBarDataProxy *self,
    const QString *rowRole,
    const QString *columnRole,
    const QString *valueRole,
    const QString *rotationRole,
    const QList<QString> *rowCategories,
    const QList<QString> *columnCategories) {
  self->remap(
      *rowRole,
      *columnRole,
      *valueRole,
      *rotationRole,
      *rowCategories,
      *columnCategories);
}

//  qsizetype QItemModelBarDataProxy::rowCategoryIndex(const QString
//      &category)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QItemModelBarDataProxy16rowCategoryIndexERK7QString(
    QItemModelBarDataProxy *self,
    const QString *category) {
  return self->rowCategoryIndex(*category);
}

//  qsizetype QItemModelBarDataProxy::columnCategoryIndex(const QString
//      &category)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QItemModelBarDataProxy19columnCategoryIndexERK7QString(
    QItemModelBarDataProxy *self,
    const QString *category) {
  return self->columnCategoryIndex(*category);
}

//  void QItemModelBarDataProxy::setRowRolePattern(const QRegularExpression
//      &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy17setRowRolePatternERK18QRegularExpression(
    QItemModelBarDataProxy *self,
    const QRegularExpression *pattern) {
  self->setRowRolePattern(*pattern);
}

//  QRegularExpression QItemModelBarDataProxy::rowRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK22QItemModelBarDataProxy14rowRolePatternEv(
    const QItemModelBarDataProxy *self) {
  return new QRegularExpression(self->rowRolePattern());
}

//  void QItemModelBarDataProxy::setColumnRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy20setColumnRolePatternERK18QRegularExpression(
    QItemModelBarDataProxy *self,
    const QRegularExpression *pattern) {
  self->setColumnRolePattern(*pattern);
}

//  QRegularExpression QItemModelBarDataProxy::columnRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK22QItemModelBarDataProxy17columnRolePatternEv(
    const QItemModelBarDataProxy *self) {
  return new QRegularExpression(self->columnRolePattern());
}

//  void QItemModelBarDataProxy::setValueRolePattern(const QRegularExpression
//      &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy19setValueRolePatternERK18QRegularExpression(
    QItemModelBarDataProxy *self,
    const QRegularExpression *pattern) {
  self->setValueRolePattern(*pattern);
}

//  QRegularExpression QItemModelBarDataProxy::valueRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK22QItemModelBarDataProxy16valueRolePatternEv(
    const QItemModelBarDataProxy *self) {
  return new QRegularExpression(self->valueRolePattern());
}

//  void QItemModelBarDataProxy::setRotationRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy22setRotationRolePatternERK18QRegularExpression(
    QItemModelBarDataProxy *self,
    const QRegularExpression *pattern) {
  self->setRotationRolePattern(*pattern);
}

//  QRegularExpression QItemModelBarDataProxy::rotationRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK22QItemModelBarDataProxy19rotationRolePatternEv(
    const QItemModelBarDataProxy *self) {
  return new QRegularExpression(self->rotationRolePattern());
}

//  void QItemModelBarDataProxy::setRowRoleReplace(const QString &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy17setRowRoleReplaceERK7QString(
    QItemModelBarDataProxy *self,
    const QString *replace) {
  self->setRowRoleReplace(*replace);
}

//  QString QItemModelBarDataProxy::rowRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy14rowRoleReplaceEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->rowRoleReplace());
}

//  void QItemModelBarDataProxy::setColumnRoleReplace(const QString &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy20setColumnRoleReplaceERK7QString(
    QItemModelBarDataProxy *self,
    const QString *replace) {
  self->setColumnRoleReplace(*replace);
}

//  QString QItemModelBarDataProxy::columnRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy17columnRoleReplaceEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->columnRoleReplace());
}

//  void QItemModelBarDataProxy::setValueRoleReplace(const QString &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy19setValueRoleReplaceERK7QString(
    QItemModelBarDataProxy *self,
    const QString *replace) {
  self->setValueRoleReplace(*replace);
}

//  QString QItemModelBarDataProxy::valueRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy16valueRoleReplaceEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->valueRoleReplace());
}

//  void QItemModelBarDataProxy::setRotationRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy22setRotationRoleReplaceERK7QString(
    QItemModelBarDataProxy *self,
    const QString *replace) {
  self->setRotationRoleReplace(*replace);
}

//  QString QItemModelBarDataProxy::rotationRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QItemModelBarDataProxy19rotationRoleReplaceEv(
    const QItemModelBarDataProxy *self) {
  return new QString(self->rotationRoleReplace());
}

//  void QItemModelBarDataProxy::setMultiMatchBehavior(QItemModelBarDataProxy
//      ::MultiMatchBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemModelBarDataProxy21setMultiMatchBehaviorENS_18MultiMatchBehaviorE(
    QItemModelBarDataProxy *self,
    QItemModelBarDataProxy::MultiMatchBehavior behavior) {
  self->setMultiMatchBehavior(behavior);
}

//  QItemModelBarDataProxy::MultiMatchBehavior
//      QItemModelBarDataProxy::multiMatchBehavior() const
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy::MultiMatchBehavior ritual_ZNK22QItemModelBarDataProxy18multiMatchBehaviorEv(
    const QItemModelBarDataProxy *self) {
  return self->multiMatchBehavior();
}

//  a Python function taken by a CuteQItemModelBarDataProxy, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelBarDataProxy(
    QItemModelBarDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelBarDataProxy *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
