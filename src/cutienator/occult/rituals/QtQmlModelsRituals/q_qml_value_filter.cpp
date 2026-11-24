//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlvaluefilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlvaluefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlValueFilter that Python can take functions over in. Every QQmlValueFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlValueFilterCall0)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlValueFilterCall1)(const void *, const QQmlSortFilterProxyModel *, int *);
typedef int (*CuteQQmlValueFilterCall2)(const void *, int *);
typedef void (*CuteQQmlValueFilterCall3)(const void *, int, int *);
typedef bool (*CuteQQmlValueFilterCall4)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef bool (*CuteQQmlValueFilterCall5)(const void *, int *);
typedef bool (*CuteQQmlValueFilterCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlValueFilterCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlValueFilterCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlValueFilterCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlValueFilterCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlValueFilterCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlValueFilterCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlValueFilterCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlValueFilter : public QQmlValueFilter {
public:
  using QQmlValueFilter::QQmlValueFilter;
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

  //  bool QQmlValueFilter::filterAcceptsRowInternal(int row, const
  //      QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2)
  //      const
  bool filterAcceptsRowInternal(
      int row,
      const QModelIndex &sourceIndex,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlValueFilterCall0 call = reinterpret_cast<CuteQQmlValueFilterCall0>(taken[0]);
      bool given = call(this, row, &sourceIndex, a2, &handled);
      if (handled) return given;
    }
    return QQmlValueFilter::filterAcceptsRowInternal(row, sourceIndex, a2);
  }

  //  void QQmlRoleFilter::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlValueFilterCall1 call = reinterpret_cast<CuteQQmlValueFilterCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlRoleFilter::update(a0);
  }

  //  int QQmlFilterBase::column() const
  int column() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlValueFilterCall2 call = reinterpret_cast<CuteQQmlValueFilterCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::column();
  }

  //  void QQmlFilterBase::setColumn(int column)
  void setColumn(int column) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlValueFilterCall3 call = reinterpret_cast<CuteQQmlValueFilterCall3>(taken[3]);
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
      CuteQQmlValueFilterCall4 call = reinterpret_cast<CuteQQmlValueFilterCall4>(taken[4]);
      bool given = call(this, a0, &a1, a2, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::filterAcceptsColumnInternal(a0, a1, a2);
  }

  //  bool QQmlFilterBase::supportColumnFiltering() const
  bool supportColumnFiltering() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlValueFilterCall5 call = reinterpret_cast<CuteQQmlValueFilterCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::supportColumnFiltering();
  }

  //  bool QQmlFilterBase::isActive() const
  bool isActive() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlValueFilterCall6 call = reinterpret_cast<CuteQQmlValueFilterCall6>(taken[6]);
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
      CuteQQmlValueFilterCall7 call = reinterpret_cast<CuteQQmlValueFilterCall7>(taken[7]);
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
      CuteQQmlValueFilterCall8 call = reinterpret_cast<CuteQQmlValueFilterCall8>(taken[8]);
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
      CuteQQmlValueFilterCall9 call = reinterpret_cast<CuteQQmlValueFilterCall9>(taken[9]);
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
      CuteQQmlValueFilterCall10 call = reinterpret_cast<CuteQQmlValueFilterCall10>(taken[10]);
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
      CuteQQmlValueFilterCall11 call = reinterpret_cast<CuteQQmlValueFilterCall11>(taken[11]);
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
      CuteQQmlValueFilterCall12 call = reinterpret_cast<CuteQQmlValueFilterCall12>(taken[12]);
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
      CuteQQmlValueFilterCall13 call = reinterpret_cast<CuteQQmlValueFilterCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlValueFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlValueFilter10metaObjectEv(
    const QQmlValueFilter *self) {
  return self->metaObject();
}

//  QString QQmlValueFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlValueFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlValueFilter::tr(s, c, n));
}

//  QQmlValueFilter::QQmlValueFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlValueFilter *ritual_ZN15QQmlValueFilterC1EP7QObject(QObject *parent) {
  return new CuteQQmlValueFilter(parent);
}

//  QQmlValueFilter::~QQmlValueFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlValueFilterD1Ev(QQmlValueFilter *self) {
  delete self;
}

//  const QVariant &QQmlValueFilter::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQmlValueFilter5valueEv(const QQmlValueFilter *self) {
  return new QVariant(self->value());
}

//  void QQmlValueFilter::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlValueFilter8setValueERK8QVariant(
    QQmlValueFilter *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  void QQmlValueFilter::resetValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlValueFilter10resetValueEv(QQmlValueFilter *self) {
  self->resetValue();
}

//  bool QQmlValueFilter::filterAcceptsRowInternal(int row, const QModelIndex
//      &sourceIndex, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlValueFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlValueFilter *self,
    int row,
    const QModelIndex *sourceIndex,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsRowInternal(row, *sourceIndex, a2);
}

//  QQmlValueFilterPrivate *QQmlValueFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlValueFilterPrivate *ritual_ZN15QQmlValueFilter6d_funcEv(
    QQmlValueFilter *self) {
  return self->d_func();
}

//  const QQmlValueFilterPrivate *QQmlValueFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlValueFilterPrivate *ritual_ZNK15QQmlValueFilter6d_funcEv(
    const QQmlValueFilter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlValueFilter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlValueFilter(
    QQmlValueFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlValueFilter *>(self)->take(key, call);
}

//  bool QQmlValueFilter::filterAcceptsRowInternal(int row, const QModelIndex
//      &sourceIndex, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlValueFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlValueFilter *self,
    int row,
    const QModelIndex *sourceIndex,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlValueFilter::filterAcceptsRowInternal(
      row,
      *sourceIndex,
      a2);
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
