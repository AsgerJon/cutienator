//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlrangefilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlrangefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlRangeFilter that Python can take functions over in. Every QQmlRangeFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlRangeFilterCall0)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlRangeFilterCall1)(const void *, const QQmlSortFilterProxyModel *, int *);
typedef int (*CuteQQmlRangeFilterCall2)(const void *, int *);
typedef void (*CuteQQmlRangeFilterCall3)(const void *, int, int *);
typedef bool (*CuteQQmlRangeFilterCall4)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef bool (*CuteQQmlRangeFilterCall5)(const void *, int *);
typedef bool (*CuteQQmlRangeFilterCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlRangeFilterCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlRangeFilterCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRangeFilterCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRangeFilterCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRangeFilterCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRangeFilterCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlRangeFilterCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlRangeFilter : public QQmlRangeFilter {
public:
  using QQmlRangeFilter::QQmlRangeFilter;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase6columnEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlFilterBase9setColumnEi")) {
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

  //  bool QQmlRangeFilter::filterAcceptsRowInternal(int row, const
  //      QModelIndex &sourceParent, const QQmlSortFilterProxyModel
  //      *proxyModel) const
  bool filterAcceptsRowInternal(
      int row,
      const QModelIndex &sourceParent,
      const QQmlSortFilterProxyModel *proxyModel) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlRangeFilterCall0 call = reinterpret_cast<CuteQQmlRangeFilterCall0>(taken[0]);
      bool given = call(this, row, &sourceParent, proxyModel, &handled);
      if (handled) return given;
    }
    return QQmlRangeFilter::filterAcceptsRowInternal(row, sourceParent, proxyModel);
  }

  //  void QQmlRoleFilter::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlRangeFilterCall1 call = reinterpret_cast<CuteQQmlRangeFilterCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlRoleFilter::update(a0);
  }

  //  int QQmlFilterBase::column() const
  int column() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlRangeFilterCall2 call = reinterpret_cast<CuteQQmlRangeFilterCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::column();
  }

  //  void QQmlFilterBase::setColumn(int column)
  void setColumn(int column) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlRangeFilterCall3 call = reinterpret_cast<CuteQQmlRangeFilterCall3>(taken[3]);
      call(this, column, &handled);
      if (handled) return;
    }
    QQmlFilterBase::setColumn(column);
  }

  //  bool QQmlFilterBase::filterAcceptsColumnInternal(int a0, const
  //      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
  bool filterAcceptsColumnInternal(
      int a0,
      const QModelIndex &a1,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlRangeFilterCall4 call = reinterpret_cast<CuteQQmlRangeFilterCall4>(taken[4]);
      bool given = call(this, a0, &a1, a2, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::filterAcceptsColumnInternal(a0, a1, a2);
  }

  //  bool QQmlFilterBase::supportColumnFiltering() const
  bool supportColumnFiltering() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlRangeFilterCall5 call = reinterpret_cast<CuteQQmlRangeFilterCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::supportColumnFiltering();
  }

  //  bool QQmlFilterBase::isActive() const
  bool isActive() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlRangeFilterCall6 call = reinterpret_cast<CuteQQmlRangeFilterCall6>(taken[6]);
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
      CuteQQmlRangeFilterCall7 call = reinterpret_cast<CuteQQmlRangeFilterCall7>(taken[7]);
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
      CuteQQmlRangeFilterCall8 call = reinterpret_cast<CuteQQmlRangeFilterCall8>(taken[8]);
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
      CuteQQmlRangeFilterCall9 call = reinterpret_cast<CuteQQmlRangeFilterCall9>(taken[9]);
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
      CuteQQmlRangeFilterCall10 call = reinterpret_cast<CuteQQmlRangeFilterCall10>(taken[10]);
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
      CuteQQmlRangeFilterCall11 call = reinterpret_cast<CuteQQmlRangeFilterCall11>(taken[11]);
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
      CuteQQmlRangeFilterCall12 call = reinterpret_cast<CuteQQmlRangeFilterCall12>(taken[12]);
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
      CuteQQmlRangeFilterCall13 call = reinterpret_cast<CuteQQmlRangeFilterCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlRangeFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlRangeFilter10metaObjectEv(
    const QQmlRangeFilter *self) {
  return self->metaObject();
}

//  QString QQmlRangeFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlRangeFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlRangeFilter::tr(s, c, n));
}

//  QQmlRangeFilter::QQmlRangeFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlRangeFilter *ritual_ZN15QQmlRangeFilterC1EP7QObject(QObject *parent) {
  return new CuteQQmlRangeFilter(parent);
}

//  QQmlRangeFilter::~QQmlRangeFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlRangeFilterD1Ev(QQmlRangeFilter *self) {
  delete self;
}

//  const QVariant &QQmlRangeFilter::minimum() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQmlRangeFilter7minimumEv(
    const QQmlRangeFilter *self) {
  return new QVariant(self->minimum());
}

//  void QQmlRangeFilter::setMinimum(const QVariant &minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlRangeFilter10setMinimumERK8QVariant(
    QQmlRangeFilter *self,
    const QVariant *minimum) {
  self->setMinimum(*minimum);
}

//  void QQmlRangeFilter::resetMinimum()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlRangeFilter12resetMinimumEv(QQmlRangeFilter *self) {
  self->resetMinimum();
}

//  const QVariant &QQmlRangeFilter::maximum() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQmlRangeFilter7maximumEv(
    const QQmlRangeFilter *self) {
  return new QVariant(self->maximum());
}

//  void QQmlRangeFilter::setMaximum(const QVariant &maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlRangeFilter10setMaximumERK8QVariant(
    QQmlRangeFilter *self,
    const QVariant *maximum) {
  self->setMaximum(*maximum);
}

//  void QQmlRangeFilter::resetMaximum()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlRangeFilter12resetMaximumEv(QQmlRangeFilter *self) {
  self->resetMaximum();
}

//  QVariant QQmlRangeFilter::exclusive(const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QQmlRangeFilter9exclusiveERK8QVariant(
    const QVariant *value) {
  return new QVariant(QQmlRangeFilter::exclusive(*value));
}

//  bool QQmlRangeFilter::filterAcceptsRowInternal(int row, const QModelIndex
//      &sourceParent, const QQmlSortFilterProxyModel *proxyModel) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlRangeFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlRangeFilter *self,
    int row,
    const QModelIndex *sourceParent,
    const QQmlSortFilterProxyModel *proxyModel) {
  return self->filterAcceptsRowInternal(row, *sourceParent, proxyModel);
}

//  QQmlRangeFilterPrivate *QQmlRangeFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlRangeFilterPrivate *ritual_ZN15QQmlRangeFilter6d_funcEv(
    QQmlRangeFilter *self) {
  return self->d_func();
}

//  const QQmlRangeFilterPrivate *QQmlRangeFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlRangeFilterPrivate *ritual_ZNK15QQmlRangeFilter6d_funcEv(
    const QQmlRangeFilter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlRangeFilter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlRangeFilter(
    QQmlRangeFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlRangeFilter *>(self)->take(key, call);
}

//  bool QQmlRangeFilter::filterAcceptsRowInternal(int row, const QModelIndex
//      &sourceParent, const QQmlSortFilterProxyModel *proxyModel) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlRangeFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlRangeFilter *self,
    int row,
    const QModelIndex *sourceParent,
    const QQmlSortFilterProxyModel *proxyModel) {
  return self->QQmlRangeFilter::filterAcceptsRowInternal(
      row,
      *sourceParent,
      proxyModel);
}
