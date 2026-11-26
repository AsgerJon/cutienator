//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qitemmodelsurfacedataproxy.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDataVisualization/qitemmodelsurfacedataproxy.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QItemModelSurfaceDataProxy that Python can take functions over in. Every QItemModelSurfaceDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelSurfaceDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelSurfaceDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemModelSurfaceDataProxy : public QItemModelSurfaceDataProxy {
public:
  using QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy;
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
      CuteQItemModelSurfaceDataProxyCall0 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall0>(taken[0]);
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
      CuteQItemModelSurfaceDataProxyCall1 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall1>(taken[1]);
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
      CuteQItemModelSurfaceDataProxyCall2 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall2>(taken[2]);
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
      CuteQItemModelSurfaceDataProxyCall3 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall3>(taken[3]);
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
      CuteQItemModelSurfaceDataProxyCall4 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall4>(taken[4]);
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
      CuteQItemModelSurfaceDataProxyCall5 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall5>(taken[5]);
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
      CuteQItemModelSurfaceDataProxyCall6 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QItemModelSurfaceDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QItemModelSurfaceDataProxy10metaObjectEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->metaObject();
}

//  void *QItemModelSurfaceDataProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QItemModelSurfaceDataProxy11qt_metacastEPKc(
    QItemModelSurfaceDataProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QItemModelSurfaceDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QItemModelSurfaceDataProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QItemModelSurfaceDataProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QItemModelSurfaceDataProxy::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QItemModelSurfaceDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemModelSurfaceDataProxy::tr(s, c, n));
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP7QObject(
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(parent);
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QAbstractItemModel
//      *itemModel, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *itemModel,
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(itemModel, parent);
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QAbstractItemModel
//      *itemModel, const QString &yPosRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QStringP7QObject(
    QAbstractItemModel *itemModel,
    const QString *yPosRole,
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(itemModel, *yPosRole, parent);
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &yPosRole, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *yPosRole,
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *yPosRole,
      parent);
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &xPosRole, const QString &yPosRole, const QString &zPosRole,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_S4_S4_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *xPosRole,
      *yPosRole,
      *zPosRole,
      parent);
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &yPosRole, const QStringList &rowCategories, const
//      QStringList &columnCategories, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_RK5QListIS2_ES8_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *yPosRole,
    const QList<QString> *rowCategories,
    const QList<QString> *columnCategories,
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *yPosRole,
      *rowCategories,
      *columnCategories,
      parent);
}

//  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QAbstractItemModel
//      *itemModel, const QString &rowRole, const QString &columnRole, const
//      QString &xPosRole, const QString &yPosRole, const QString &zPosRole,
//      const QStringList &rowCategories, const QStringList
//      &columnCategories, QObject *parent)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QStringS4_S4_S4_S4_RK5QListIS2_ES8_P7QObject(
    QAbstractItemModel *itemModel,
    const QString *rowRole,
    const QString *columnRole,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    const QList<QString> *rowCategories,
    const QList<QString> *columnCategories,
    QObject *parent) {
  return new CuteQItemModelSurfaceDataProxy(
      itemModel,
      *rowRole,
      *columnRole,
      *xPosRole,
      *yPosRole,
      *zPosRole,
      *rowCategories,
      *columnCategories,
      parent);
}

//  QItemModelSurfaceDataProxy::~QItemModelSurfaceDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxyD1Ev(
    QItemModelSurfaceDataProxy *self) {
  delete self;
}

//  void QItemModelSurfaceDataProxy::setItemModel(QAbstractItemModel
//      *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy12setItemModelEP18QAbstractItemModel(
    QItemModelSurfaceDataProxy *self,
    QAbstractItemModel *itemModel) {
  self->setItemModel(itemModel);
}

//  QAbstractItemModel *QItemModelSurfaceDataProxy::itemModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK26QItemModelSurfaceDataProxy9itemModelEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->itemModel();
}

//  void QItemModelSurfaceDataProxy::setRowRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy10setRowRoleERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->setRowRole(*role);
}

//  QString QItemModelSurfaceDataProxy::rowRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy7rowRoleEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->rowRole());
}

//  void QItemModelSurfaceDataProxy::setColumnRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy13setColumnRoleERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->setColumnRole(*role);
}

//  QString QItemModelSurfaceDataProxy::columnRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy10columnRoleEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->columnRole());
}

//  void QItemModelSurfaceDataProxy::setXPosRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy11setXPosRoleERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->setXPosRole(*role);
}

//  QString QItemModelSurfaceDataProxy::xPosRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy8xPosRoleEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->xPosRole());
}

//  void QItemModelSurfaceDataProxy::setYPosRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy11setYPosRoleERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->setYPosRole(*role);
}

//  QString QItemModelSurfaceDataProxy::yPosRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy8yPosRoleEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->yPosRole());
}

//  void QItemModelSurfaceDataProxy::setZPosRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy11setZPosRoleERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->setZPosRole(*role);
}

//  QString QItemModelSurfaceDataProxy::zPosRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy8zPosRoleEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->zPosRole());
}

//  void QItemModelSurfaceDataProxy::setRowCategories(const QStringList
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy16setRowCategoriesERK5QListI7QStringE(
    QItemModelSurfaceDataProxy *self,
    const QList<QString> *categories) {
  self->setRowCategories(*categories);
}

//  QStringList QItemModelSurfaceDataProxy::rowCategories() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QItemModelSurfaceDataProxy13rowCategoriesEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QList<QString>(self->rowCategories());
}

//  void QItemModelSurfaceDataProxy::setColumnCategories(const QStringList
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy19setColumnCategoriesERK5QListI7QStringE(
    QItemModelSurfaceDataProxy *self,
    const QList<QString> *categories) {
  self->setColumnCategories(*categories);
}

//  QStringList QItemModelSurfaceDataProxy::columnCategories() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QItemModelSurfaceDataProxy16columnCategoriesEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QList<QString>(self->columnCategories());
}

//  void QItemModelSurfaceDataProxy::setUseModelCategories(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy21setUseModelCategoriesEb(
    QItemModelSurfaceDataProxy *self,
    bool enable) {
  self->setUseModelCategories(enable);
}

//  bool QItemModelSurfaceDataProxy::useModelCategories() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QItemModelSurfaceDataProxy18useModelCategoriesEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->useModelCategories();
}

//  void QItemModelSurfaceDataProxy::setAutoRowCategories(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy20setAutoRowCategoriesEb(
    QItemModelSurfaceDataProxy *self,
    bool enable) {
  self->setAutoRowCategories(enable);
}

//  bool QItemModelSurfaceDataProxy::autoRowCategories() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QItemModelSurfaceDataProxy17autoRowCategoriesEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->autoRowCategories();
}

//  void QItemModelSurfaceDataProxy::setAutoColumnCategories(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy23setAutoColumnCategoriesEb(
    QItemModelSurfaceDataProxy *self,
    bool enable) {
  self->setAutoColumnCategories(enable);
}

//  bool QItemModelSurfaceDataProxy::autoColumnCategories() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QItemModelSurfaceDataProxy20autoColumnCategoriesEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->autoColumnCategories();
}

//  void QItemModelSurfaceDataProxy::remap(const QString &rowRole, const
//      QString &columnRole, const QString &xPosRole, const QString
//      &yPosRole, const QString &zPosRole, const QStringList &rowCategories,
//      const QStringList &columnCategories)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy5remapERK7QStringS2_S2_S2_S2_RK5QListIS0_ES6_(
    QItemModelSurfaceDataProxy *self,
    const QString *rowRole,
    const QString *columnRole,
    const QString *xPosRole,
    const QString *yPosRole,
    const QString *zPosRole,
    const QList<QString> *rowCategories,
    const QList<QString> *columnCategories) {
  self->remap(
      *rowRole,
      *columnRole,
      *xPosRole,
      *yPosRole,
      *zPosRole,
      *rowCategories,
      *columnCategories);
}

//  int QItemModelSurfaceDataProxy::rowCategoryIndex(const QString &category)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QItemModelSurfaceDataProxy16rowCategoryIndexERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *category) {
  return self->rowCategoryIndex(*category);
}

//  int QItemModelSurfaceDataProxy::columnCategoryIndex(const QString
//      &category)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QItemModelSurfaceDataProxy19columnCategoryIndexERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *category) {
  return self->columnCategoryIndex(*category);
}

//  void QItemModelSurfaceDataProxy::setRowRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy17setRowRolePatternERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->setRowRolePattern(*pattern);
}

//  QRegularExpression QItemModelSurfaceDataProxy::rowRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelSurfaceDataProxy14rowRolePatternEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QRegularExpression(self->rowRolePattern());
}

//  void QItemModelSurfaceDataProxy::setColumnRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy20setColumnRolePatternERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->setColumnRolePattern(*pattern);
}

//  QRegularExpression QItemModelSurfaceDataProxy::columnRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelSurfaceDataProxy17columnRolePatternEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QRegularExpression(self->columnRolePattern());
}

//  void QItemModelSurfaceDataProxy::setXPosRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy18setXPosRolePatternERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->setXPosRolePattern(*pattern);
}

//  QRegularExpression QItemModelSurfaceDataProxy::xPosRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelSurfaceDataProxy15xPosRolePatternEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QRegularExpression(self->xPosRolePattern());
}

//  void QItemModelSurfaceDataProxy::setYPosRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy18setYPosRolePatternERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->setYPosRolePattern(*pattern);
}

//  QRegularExpression QItemModelSurfaceDataProxy::yPosRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelSurfaceDataProxy15yPosRolePatternEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QRegularExpression(self->yPosRolePattern());
}

//  void QItemModelSurfaceDataProxy::setZPosRolePattern(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy18setZPosRolePatternERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->setZPosRolePattern(*pattern);
}

//  QRegularExpression QItemModelSurfaceDataProxy::zPosRolePattern() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK26QItemModelSurfaceDataProxy15zPosRolePatternEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QRegularExpression(self->zPosRolePattern());
}

//  void QItemModelSurfaceDataProxy::setRowRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy17setRowRoleReplaceERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->setRowRoleReplace(*replace);
}

//  QString QItemModelSurfaceDataProxy::rowRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy14rowRoleReplaceEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->rowRoleReplace());
}

//  void QItemModelSurfaceDataProxy::setColumnRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy20setColumnRoleReplaceERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->setColumnRoleReplace(*replace);
}

//  QString QItemModelSurfaceDataProxy::columnRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy17columnRoleReplaceEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->columnRoleReplace());
}

//  void QItemModelSurfaceDataProxy::setXPosRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy18setXPosRoleReplaceERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->setXPosRoleReplace(*replace);
}

//  QString QItemModelSurfaceDataProxy::xPosRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy15xPosRoleReplaceEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->xPosRoleReplace());
}

//  void QItemModelSurfaceDataProxy::setYPosRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy18setYPosRoleReplaceERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->setYPosRoleReplace(*replace);
}

//  QString QItemModelSurfaceDataProxy::yPosRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy15yPosRoleReplaceEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->yPosRoleReplace());
}

//  void QItemModelSurfaceDataProxy::setZPosRoleReplace(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy18setZPosRoleReplaceERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->setZPosRoleReplace(*replace);
}

//  QString QItemModelSurfaceDataProxy::zPosRoleReplace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QItemModelSurfaceDataProxy15zPosRoleReplaceEv(
    const QItemModelSurfaceDataProxy *self) {
  return new QString(self->zPosRoleReplace());
}

//  void QItemModelSurfaceDataProxy::setMultiMatchBehavior(MultiMatchBehavior
//      behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy21setMultiMatchBehaviorENS_18MultiMatchBehaviorE(
    QItemModelSurfaceDataProxy *self,
    QItemModelSurfaceDataProxy::MultiMatchBehavior behavior) {
  self->setMultiMatchBehavior(behavior);
}

//  MultiMatchBehavior QItemModelSurfaceDataProxy::multiMatchBehavior() const
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy::MultiMatchBehavior ritual_ZNK26QItemModelSurfaceDataProxy18multiMatchBehaviorEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->multiMatchBehavior();
}

//  void QItemModelSurfaceDataProxy::itemModelChanged(const
//      QAbstractItemModel *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy16itemModelChangedEPK18QAbstractItemModel(
    QItemModelSurfaceDataProxy *self,
    const QAbstractItemModel *itemModel) {
  self->itemModelChanged(itemModel);
}

//  void QItemModelSurfaceDataProxy::rowRoleChanged(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy14rowRoleChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->rowRoleChanged(*role);
}

//  void QItemModelSurfaceDataProxy::columnRoleChanged(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy17columnRoleChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->columnRoleChanged(*role);
}

//  void QItemModelSurfaceDataProxy::xPosRoleChanged(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy15xPosRoleChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->xPosRoleChanged(*role);
}

//  void QItemModelSurfaceDataProxy::yPosRoleChanged(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy15yPosRoleChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->yPosRoleChanged(*role);
}

//  void QItemModelSurfaceDataProxy::zPosRoleChanged(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy15zPosRoleChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *role) {
  self->zPosRoleChanged(*role);
}

//  void QItemModelSurfaceDataProxy::rowCategoriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy20rowCategoriesChangedEv(
    QItemModelSurfaceDataProxy *self) {
  self->rowCategoriesChanged();
}

//  void QItemModelSurfaceDataProxy::columnCategoriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy23columnCategoriesChangedEv(
    QItemModelSurfaceDataProxy *self) {
  self->columnCategoriesChanged();
}

//  void QItemModelSurfaceDataProxy::useModelCategoriesChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy25useModelCategoriesChangedEb(
    QItemModelSurfaceDataProxy *self,
    bool enable) {
  self->useModelCategoriesChanged(enable);
}

//  void QItemModelSurfaceDataProxy::autoRowCategoriesChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy24autoRowCategoriesChangedEb(
    QItemModelSurfaceDataProxy *self,
    bool enable) {
  self->autoRowCategoriesChanged(enable);
}

//  void QItemModelSurfaceDataProxy::autoColumnCategoriesChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy27autoColumnCategoriesChangedEb(
    QItemModelSurfaceDataProxy *self,
    bool enable) {
  self->autoColumnCategoriesChanged(enable);
}

//  void QItemModelSurfaceDataProxy::rowRolePatternChanged(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy21rowRolePatternChangedERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->rowRolePatternChanged(*pattern);
}

//  void QItemModelSurfaceDataProxy::columnRolePatternChanged(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy24columnRolePatternChangedERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->columnRolePatternChanged(*pattern);
}

//  void QItemModelSurfaceDataProxy::xPosRolePatternChanged(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy22xPosRolePatternChangedERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->xPosRolePatternChanged(*pattern);
}

//  void QItemModelSurfaceDataProxy::yPosRolePatternChanged(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy22yPosRolePatternChangedERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->yPosRolePatternChanged(*pattern);
}

//  void QItemModelSurfaceDataProxy::zPosRolePatternChanged(const
//      QRegularExpression &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy22zPosRolePatternChangedERK18QRegularExpression(
    QItemModelSurfaceDataProxy *self,
    const QRegularExpression *pattern) {
  self->zPosRolePatternChanged(*pattern);
}

//  void QItemModelSurfaceDataProxy::rowRoleReplaceChanged(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy21rowRoleReplaceChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->rowRoleReplaceChanged(*replace);
}

//  void QItemModelSurfaceDataProxy::columnRoleReplaceChanged(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy24columnRoleReplaceChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->columnRoleReplaceChanged(*replace);
}

//  void QItemModelSurfaceDataProxy::xPosRoleReplaceChanged(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy22xPosRoleReplaceChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->xPosRoleReplaceChanged(*replace);
}

//  void QItemModelSurfaceDataProxy::yPosRoleReplaceChanged(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy22yPosRoleReplaceChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->yPosRoleReplaceChanged(*replace);
}

//  void QItemModelSurfaceDataProxy::zPosRoleReplaceChanged(const QString
//      &replace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy22zPosRoleReplaceChangedERK7QString(
    QItemModelSurfaceDataProxy *self,
    const QString *replace) {
  self->zPosRoleReplaceChanged(*replace);
}

//  void
//      QItemModelSurfaceDataProxy::multiMatchBehaviorChanged(MultiMatchBehav
//      ior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemModelSurfaceDataProxy25multiMatchBehaviorChangedENS_18MultiMatchBehaviorE(
    QItemModelSurfaceDataProxy *self,
    QItemModelSurfaceDataProxy::MultiMatchBehavior behavior) {
  self->multiMatchBehaviorChanged(behavior);
}

//  QItemModelSurfaceDataProxyPrivate *QItemModelSurfaceDataProxy::dptr()
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxyPrivate *ritual_ZN26QItemModelSurfaceDataProxy4dptrEv(
    QItemModelSurfaceDataProxy *self) {
  return self->dptr();
}

//  const QItemModelSurfaceDataProxyPrivate
//      *QItemModelSurfaceDataProxy::dptrc() const
extern "C" Q_DECL_EXPORT
const QItemModelSurfaceDataProxyPrivate *ritual_ZNK26QItemModelSurfaceDataProxy5dptrcEv(
    const QItemModelSurfaceDataProxy *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQItemModelSurfaceDataProxy, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelSurfaceDataProxy(
    QItemModelSurfaceDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelSurfaceDataProxy *>(self)->take(key, call);
}
