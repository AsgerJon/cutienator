//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfunctionfilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlfunctionfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlFunctionFilter that Python can take functions over in. Every QQmlFunctionFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlFunctionFilterCall0)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlFunctionFilterCall1)(const void *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlFunctionFilterCall2)(const void *, int *);
typedef void (*CuteQQmlFunctionFilterCall3)(const void *, int *);
typedef int (*CuteQQmlFunctionFilterCall4)(const void *, int *);
typedef void (*CuteQQmlFunctionFilterCall5)(const void *, int, int *);
typedef bool (*CuteQQmlFunctionFilterCall6)(const void *, int, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef bool (*CuteQQmlFunctionFilterCall7)(const void *, int *);
typedef bool (*CuteQQmlFunctionFilterCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlFunctionFilterCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlFunctionFilterCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionFilterCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionFilterCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionFilterCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionFilterCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFunctionFilterCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlFunctionFilter : public QQmlFunctionFilter {
public:
  using QQmlFunctionFilter::QQmlFunctionFilter;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase6columnEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlFilterBase9setColumnEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase22supportColumnFilteringEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlFilterBase8isActiveEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQmlFunctionFilter::filterAcceptsRowInternal(int row, const
  //      QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2)
  //      const
  bool filterAcceptsRowInternal(
      int row,
      const QModelIndex &sourceIndex,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall0 call = reinterpret_cast<CuteQQmlFunctionFilterCall0>(taken[0]);
      bool given = call(this, row, &sourceIndex, a2, &handled);
      if (handled) return given;
    }
    return QQmlFunctionFilter::filterAcceptsRowInternal(row, sourceIndex, a2);
  }

  //  void QQmlFunctionFilter::update(const QQmlSortFilterProxyModel
  //      *proxyModel)
  void update(const QQmlSortFilterProxyModel *proxyModel) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall1 call = reinterpret_cast<CuteQQmlFunctionFilterCall1>(taken[1]);
      call(this, proxyModel, &handled);
      if (handled) return;
    }
    QQmlFunctionFilter::update(proxyModel);
  }

  //  void QQmlFunctionFilter::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall2 call = reinterpret_cast<CuteQQmlFunctionFilterCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlFunctionFilter::classBegin();
  }

  //  void QQmlFunctionFilter::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall3 call = reinterpret_cast<CuteQQmlFunctionFilterCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlFunctionFilter::componentComplete();
  }

  //  int QQmlFilterBase::column() const
  int column() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall4 call = reinterpret_cast<CuteQQmlFunctionFilterCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::column();
  }

  //  void QQmlFilterBase::setColumn(int column)
  void setColumn(int column) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall5 call = reinterpret_cast<CuteQQmlFunctionFilterCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall6 call = reinterpret_cast<CuteQQmlFunctionFilterCall6>(taken[6]);
      bool given = call(this, a0, &a1, a2, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::filterAcceptsColumnInternal(a0, a1, a2);
  }

  //  bool QQmlFilterBase::supportColumnFiltering() const
  bool supportColumnFiltering() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall7 call = reinterpret_cast<CuteQQmlFunctionFilterCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::supportColumnFiltering();
  }

  //  bool QQmlFilterBase::isActive() const
  bool isActive() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall8 call = reinterpret_cast<CuteQQmlFunctionFilterCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlFilterBase::isActive();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall9 call = reinterpret_cast<CuteQQmlFunctionFilterCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall10 call = reinterpret_cast<CuteQQmlFunctionFilterCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall11 call = reinterpret_cast<CuteQQmlFunctionFilterCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall12 call = reinterpret_cast<CuteQQmlFunctionFilterCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall13 call = reinterpret_cast<CuteQQmlFunctionFilterCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall14 call = reinterpret_cast<CuteQQmlFunctionFilterCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlFunctionFilterCall15 call = reinterpret_cast<CuteQQmlFunctionFilterCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlFunctionFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQmlFunctionFilter10metaObjectEv(
    const QQmlFunctionFilter *self) {
  return self->metaObject();
}

//  void *QQmlFunctionFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQmlFunctionFilter11qt_metacastEPKc(
    QQmlFunctionFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlFunctionFilter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQmlFunctionFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlFunctionFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlFunctionFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlFunctionFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlFunctionFilter::tr(s, c, n));
}

//  QQmlFunctionFilter::QQmlFunctionFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlFunctionFilter *ritual_ZN18QQmlFunctionFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlFunctionFilter(parent);
}

//  QQmlFunctionFilter::~QQmlFunctionFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionFilterD1Ev(QQmlFunctionFilter *self) {
  delete self;
}

//  bool QQmlFunctionFilter::filterAcceptsRowInternal(int row, const
//      QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlFunctionFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFunctionFilter *self,
    int row,
    const QModelIndex *sourceIndex,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsRowInternal(row, *sourceIndex, a2);
}

//  void QQmlFunctionFilter::update(const QQmlSortFilterProxyModel
//      *proxyModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionFilter6updateEPK24QQmlSortFilterProxyModel(
    QQmlFunctionFilter *self,
    const QQmlSortFilterProxyModel *proxyModel) {
  self->update(proxyModel);
}

//  void QQmlFunctionFilter::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionFilter10classBeginEv(QQmlFunctionFilter *self) {
  self->classBegin();
}

//  void QQmlFunctionFilter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlFunctionFilter17componentCompleteEv(
    QQmlFunctionFilter *self) {
  self->componentComplete();
}

//  QQmlFunctionFilterPrivate *QQmlFunctionFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlFunctionFilterPrivate *ritual_ZN18QQmlFunctionFilter6d_funcEv(
    QQmlFunctionFilter *self) {
  return self->d_func();
}

//  const QQmlFunctionFilterPrivate *QQmlFunctionFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlFunctionFilterPrivate *ritual_ZNK18QQmlFunctionFilter6d_funcEv(
    const QQmlFunctionFilter *self) {
  return self->d_func();
}

//  QQmlFunctionFilter as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlFunctionFilter_QQmlParserStatus(
    QQmlFunctionFilter *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlFunctionFilter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlFunctionFilter(
    QQmlFunctionFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlFunctionFilter *>(self)->take(key, call);
}

//  bool QQmlFunctionFilter::filterAcceptsRowInternal(int row, const
//      QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QQmlFunctionFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFunctionFilter *self,
    int row,
    const QModelIndex *sourceIndex,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlFunctionFilter::filterAcceptsRowInternal(
      row,
      *sourceIndex,
      a2);
}

//  void QQmlFunctionFilter::update(const QQmlSortFilterProxyModel
//      *proxyModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlFunctionFilter6updateEPK24QQmlSortFilterProxyModel(
    QQmlFunctionFilter *self,
    const QQmlSortFilterProxyModel *proxyModel) {
  self->QQmlFunctionFilter::update(proxyModel);
}

//  void QQmlFunctionFilter::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlFunctionFilter10classBeginEv(
    QQmlFunctionFilter *self) {
  self->QQmlFunctionFilter::classBegin();
}

//  void QQmlFunctionFilter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlFunctionFilter17componentCompleteEv(
    QQmlFunctionFilter *self) {
  self->QQmlFunctionFilter::componentComplete();
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
