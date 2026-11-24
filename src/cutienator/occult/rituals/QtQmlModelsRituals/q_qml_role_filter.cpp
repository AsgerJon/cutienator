//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlrolefilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlrolefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlRoleFilter that Python can take functions over in. Every QQmlRoleFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlRoleFilterCall0)(const void *, const QQmlSortFilterProxyModel *, int *);
typedef int (*CuteQQmlRoleFilterCall1)(const void *, int *);
typedef void (*CuteQQmlRoleFilterCall2)(const void *, int, int *);
typedef bool (*CuteQQmlRoleFilterCall3)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef bool (*CuteQQmlRoleFilterCall4)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef bool (*CuteQQmlRoleFilterCall5)(const void *, int *);
typedef bool (*CuteQQmlRoleFilterCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlRoleFilterCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlRoleFilterCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleFilterCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleFilterCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleFilterCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleFilterCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRoleFilterCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlRoleFilter : public QQmlRoleFilter {
public:
  using QQmlRoleFilter::QQmlRoleFilter;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase6columnEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlFilterBase9setColumnEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase22supportColumnFilteringEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase8isActiveEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQmlRoleFilter::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlRoleFilterCall0 call = reinterpret_cast<CuteQQmlRoleFilterCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlRoleFilter::update(a0);
  }

  //  int QQmlFilterBase::column() const
  int column() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlRoleFilterCall1 call = reinterpret_cast<CuteQQmlRoleFilterCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::column();
  }

  //  void QQmlFilterBase::setColumn(int column)
  void setColumn(int column) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlRoleFilterCall2 call = reinterpret_cast<CuteQQmlRoleFilterCall2>(taken[2]);
      call(this, column, &handled);
      if (handled) return;
    }
    QQmlFilterBase::setColumn(column);
  }

  //  bool QQmlFilterBase::filterAcceptsRowInternal(int a0, const
  //      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
  bool filterAcceptsRowInternal(
      int a0,
      const QModelIndex &a1,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlRoleFilterCall3 call = reinterpret_cast<CuteQQmlRoleFilterCall3>(taken[3]);
      bool given = call(this, a0, &a1, a2, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::filterAcceptsRowInternal(a0, a1, a2);
  }

  //  bool QQmlFilterBase::filterAcceptsColumnInternal(int a0, const
  //      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
  bool filterAcceptsColumnInternal(
      int a0,
      const QModelIndex &a1,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlRoleFilterCall4 call = reinterpret_cast<CuteQQmlRoleFilterCall4>(taken[4]);
      bool given = call(this, a0, &a1, a2, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::filterAcceptsColumnInternal(a0, a1, a2);
  }

  //  bool QQmlFilterBase::supportColumnFiltering() const
  bool supportColumnFiltering() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlRoleFilterCall5 call = reinterpret_cast<CuteQQmlRoleFilterCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::supportColumnFiltering();
  }

  //  bool QQmlFilterBase::isActive() const
  bool isActive() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlRoleFilterCall6 call = reinterpret_cast<CuteQQmlRoleFilterCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::isActive();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlRoleFilterCall7 call = reinterpret_cast<CuteQQmlRoleFilterCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlRoleFilterCall8 call = reinterpret_cast<CuteQQmlRoleFilterCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlRoleFilterCall9 call = reinterpret_cast<CuteQQmlRoleFilterCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlRoleFilterCall10 call = reinterpret_cast<CuteQQmlRoleFilterCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlRoleFilterCall11 call = reinterpret_cast<CuteQQmlRoleFilterCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlRoleFilterCall12 call = reinterpret_cast<CuteQQmlRoleFilterCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlRoleFilterCall13 call = reinterpret_cast<CuteQQmlRoleFilterCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlRoleFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlRoleFilter10metaObjectEv(
    const QQmlRoleFilter *self) {
  return self->metaObject();
}

//  QString QQmlRoleFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlRoleFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlRoleFilter::tr(s, c, n));
}

//  void QQmlRoleFilter::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleFilter24qt_qmlMarker_uncreatableEv(
    QQmlRoleFilter *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQmlRoleFilter::QQmlRoleFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlRoleFilter *ritual_ZN14QQmlRoleFilterC1EP7QObject(QObject *parent) {
  return new CuteQQmlRoleFilter(parent);
}

//  QQmlRoleFilter::QQmlRoleFilter(QQmlFilterBasePrivate *priv, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlRoleFilter *ritual_ZN14QQmlRoleFilterC1EP21QQmlFilterBasePrivateP7QObject(
    QQmlFilterBasePrivate *priv,
    QObject *parent) {
  return new CuteQQmlRoleFilter(priv, parent);
}

//  QQmlRoleFilter::~QQmlRoleFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleFilterD1Ev(QQmlRoleFilter *self) {
  delete self;
}

//  const QString &QQmlRoleFilter::roleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlRoleFilter8roleNameEv(const QQmlRoleFilter *self) {
  return new QString(self->roleName());
}

//  void QQmlRoleFilter::setRoleName(const QString &roleName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleFilter11setRoleNameERK7QString(
    QQmlRoleFilter *self,
    const QString *roleName) {
  self->setRoleName(*roleName);
}

//  void QQmlRoleFilter::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlRoleFilter6updateEPK24QQmlSortFilterProxyModel(
    QQmlRoleFilter *self,
    const QQmlSortFilterProxyModel *a0) {
  self->update(a0);
}

//  int QQmlRoleFilter::itemRole(const QQmlSortFilterProxyModel *proxyModel)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlRoleFilter8itemRoleEPK24QQmlSortFilterProxyModel(
    const QQmlRoleFilter *self,
    const QQmlSortFilterProxyModel *proxyModel) {
  return self->itemRole(proxyModel);
}

//  QQmlRoleFilterPrivate *QQmlRoleFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlRoleFilterPrivate *ritual_ZN14QQmlRoleFilter6d_funcEv(
    QQmlRoleFilter *self) {
  return self->d_func();
}

//  const QQmlRoleFilterPrivate *QQmlRoleFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlRoleFilterPrivate *ritual_ZNK14QQmlRoleFilter6d_funcEv(
    const QQmlRoleFilter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlRoleFilter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlRoleFilter(
    QQmlRoleFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlRoleFilter *>(self)->take(key, call);
}

//  void QQmlRoleFilter::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlRoleFilter6updateEPK24QQmlSortFilterProxyModel(
    QQmlRoleFilter *self,
    const QQmlSortFilterProxyModel *a0) {
  self->QQmlRoleFilter::update(a0);
}
