//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsorterbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qcompare.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmlsortercompositor_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 210, as _ZN27QQmlSorterCompositorPrivate18resetPrimarySorterEv
inline void QQmlSorterCompositorPrivate::resetPrimarySorter()
{
    if (!m_primarySorter) {
        if (!m_effectiveSorters.isEmpty()) {
            // Set the primary sort column and its order to the proxy model
            const auto *sorter = m_effectiveSorters.at(0);
            m_sfpmModel->setPrimarySortOrder(sorter->sortOrder());
            m_sfpmModel->setPrimarySortColumn(sorter->column());
        } else {
            // By default reset the  sort order to ascending order and the
            // column to 0
            m_sfpmModel->setPrimarySortOrder(Qt::AscendingOrder);
            m_sfpmModel->setPrimarySortColumn(0);
        }
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 25, as _ZN20QQmlSorterCompositorD1Ev
inline QQmlSorterCompositor::~QQmlSorterCompositor()
{

}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 109, as _ZN20QQmlSorterCompositor7sortersEv
inline QList<QQmlSorterBase *> QQmlSorterCompositor::sorters()
{
    Q_D(QQmlSorterCompositor);
    return d->m_sorters;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 176, as _ZNK20QQmlSorterCompositor8lessThanERK11QModelIndexS2_PK24QQmlSortFilterProxyModel
inline bool QQmlSorterCompositor::lessThan(const QModelIndex& sourceLeft, const QModelIndex& sourceRight, const QQmlSortFilterProxyModel *proxyModel) const
{
    Q_D(const QQmlSorterCompositor);
    for (const auto &sorter : d->m_effectiveSorters) {
        const int sortSection = sorter->column();
        if ((sortSection > -1) && (sortSection < proxyModel->sourceModel()->columnCount())) {
            const auto *sourceModel = proxyModel->sourceModel();
            const QPartialOrdering result = sorter->compare(sourceModel->index(sourceLeft.row(), sortSection),
                                                            sourceModel->index(sourceRight.row(), sortSection),
                                                            proxyModel);
            if (result == QPartialOrdering::Less || result == QPartialOrdering::Greater) {
                auto *priv = static_cast<const QQmlSortFilterProxyModelPrivate *>(QQmlSortFilterProxyModelPrivate::get(proxyModel));
                return (priv->m_sortOrder == sorter->sortOrder()) ? result < 0 : result > 0;
            }
        }
    }
    // Verify the index order when the ordering is either equal or unordered
    return sourceLeft.row() < sourceRight.row();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 145, as _ZN20QQmlSorterCompositor13updateSortersEv
inline void QQmlSorterCompositor::updateSorters()
{
    Q_D(QQmlSorterCompositor);
    // Update sorters that has dependency with the model data to determine
    // whether it needs to be included or not
    for (auto &sorter: d->m_sorters)
        sorter->update(d->m_sfpmModel);
    updateCache();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 125, as _ZN20QQmlSorterCompositor22updateEffectiveSortersEv
inline void QQmlSorterCompositor::updateEffectiveSorters()
{
    Q_D(QQmlSorterCompositor);

    if (!d->m_primarySorter || !d->m_primarySorter->enabled()) {
        updateCache();
        return;
    }

    QList<QQmlSorterBase *> sorters;
    sorters.append(d->m_primarySorter);
    std::copy_if(d->m_effectiveSorters.constBegin(), d->m_effectiveSorters.constEnd(),
                 std::back_inserter(sorters), [d](QQmlSorterBase *sorter){
                     // Consider only the filters that are enabled and exclude the primary
                     // sorter as its already added to the list
                     return (sorter != d->m_primarySorter);
                 });
    d->m_effectiveSorters = sorters;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 88, as _ZN20QQmlSorterCompositor5countEv
inline qsizetype QQmlSorterCompositor::count()
{
    Q_D(QQmlSorterCompositor);
    return d->m_sorters.count();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 94, as _ZN20QQmlSorterCompositor2atEx
inline QQmlSorterBase* QQmlSorterCompositor::at(qsizetype index)
{
    Q_D(QQmlSorterCompositor);
    return d->m_sorters.at(index);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 100, as _ZN20QQmlSorterCompositor5clearEv
inline void QQmlSorterCompositor::clear()
{
    Q_D(QQmlSorterCompositor);
    d->m_effectiveSorters.clear();
    d->m_sorters.clear();
    // Emit the filter changed signal as we cleared the filter list
    emit d->m_sfpmModel->sortersChanged();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 155, as _ZN20QQmlSorterCompositor11updateCacheEv
inline void QQmlSorterCompositor::updateCache()
{
    Q_D(QQmlSorterCompositor);
    // Clear the existing cache
    d->m_effectiveSorters.clear();
    if (d->m_sfpmModel && d->m_sfpmModel->sourceModel()) {
        // Sort the filter according to their priority
        QList<QQmlSorterBase *> sorters = d->m_sorters;
        std::stable_sort(sorters.begin(), sorters.end(),
                [](QQmlSorterBase *sorterLeft, QQmlSorterBase *sorterRight) {
                        return sorterLeft->priority() < sorterRight->priority();
                });
        // Cache only the filters that are need to be evaluated (in order)
        std::copy_if(sorters.begin(), sorters.end(), std::back_inserter(d->m_effectiveSorters),
                [](QQmlSorterBase *sorter) { return sorter->enabled(); });
        // If there is no primary sorter set by the user explicitly, reset the
        // primary sorter according to the sorters in the lists
        d->resetPrimarySorter();
    }
}
//  -----------------------------------------------------------------------

//  A QQmlSorterCompositor that Python can take functions over in. Every QQmlSorterCompositor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPartialOrdering * (*CuteQQmlSorterCompositorCall0)(const void *, const QModelIndex *, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlSorterCompositorCall1)(const void *, const QQmlSortFilterProxyModel *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSorterCompositorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSorterCompositorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSorterCompositorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSorterCompositorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSorterCompositorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSorterCompositorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSorterCompositorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlSorterCompositor : public QQmlSorterCompositor {
public:
  using QQmlSorterCompositor::QQmlSorterCompositor;
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

  //  QPartialOrdering QQmlSorterCompositor::compare(const QModelIndex &a0,
  //      const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
  QPartialOrdering compare(
      const QModelIndex &a0,
      const QModelIndex &a1,
      const QQmlSortFilterProxyModel *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSorterCompositorCall0 call = reinterpret_cast<CuteQQmlSorterCompositorCall0>(taken[0]);
      const QPartialOrdering * given = call(this, &a0, &a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QQmlSorterCompositor::compare(a0, a1, a2);
  }

  //  void QQmlSorterBase::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSorterCompositorCall1 call = reinterpret_cast<CuteQQmlSorterCompositorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlSorterBase::update(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSorterCompositorCall2 call = reinterpret_cast<CuteQQmlSorterCompositorCall2>(taken[2]);
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
      CuteQQmlSorterCompositorCall3 call = reinterpret_cast<CuteQQmlSorterCompositorCall3>(taken[3]);
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
      CuteQQmlSorterCompositorCall4 call = reinterpret_cast<CuteQQmlSorterCompositorCall4>(taken[4]);
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
      CuteQQmlSorterCompositorCall5 call = reinterpret_cast<CuteQQmlSorterCompositorCall5>(taken[5]);
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
      CuteQQmlSorterCompositorCall6 call = reinterpret_cast<CuteQQmlSorterCompositorCall6>(taken[6]);
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
      CuteQQmlSorterCompositorCall7 call = reinterpret_cast<CuteQQmlSorterCompositorCall7>(taken[7]);
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
      CuteQQmlSorterCompositorCall8 call = reinterpret_cast<CuteQQmlSorterCompositorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlSorterCompositor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlSorterCompositor10metaObjectEv(
    const QQmlSorterCompositor *self) {
  return self->metaObject();
}

//  void QQmlSorterCompositor::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor22qt_qmlMarker_anonymousEv(
    QQmlSorterCompositor *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlSorterCompositor::~QQmlSorterCompositor()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositorD1Ev(QQmlSorterCompositor *self) {
  delete self;
}

//  QList<QQmlSorterBase *> QQmlSorterCompositor::sorters()
extern "C" Q_DECL_EXPORT
QList<QQmlSorterBase *> *ritual_ZN20QQmlSorterCompositor7sortersEv(
    QQmlSorterCompositor *self) {
  return new QList<QQmlSorterBase *>(self->sorters());
}

//  QPartialOrdering QQmlSorterCompositor::compare(const QModelIndex &a0,
//      const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZNK20QQmlSorterCompositor7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlSorterCompositor *self,
    const QModelIndex *a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return new QPartialOrdering(self->compare(*a0, *a1, a2));
}

//  bool QQmlSorterCompositor::lessThan(const QModelIndex &sourceLeft, const
//      QModelIndex &sourceRight, const QQmlSortFilterProxyModel *proxyModel)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlSorterCompositor8lessThanERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlSorterCompositor *self,
    const QModelIndex *sourceLeft,
    const QModelIndex *sourceRight,
    const QQmlSortFilterProxyModel *proxyModel) {
  return self->lessThan(*sourceLeft, *sourceRight, proxyModel);
}

//  void QQmlSorterCompositor::updateSorters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor13updateSortersEv(
    QQmlSorterCompositor *self) {
  self->updateSorters();
}

//  void QQmlSorterCompositor::updateEffectiveSorters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor22updateEffectiveSortersEv(
    QQmlSorterCompositor *self) {
  self->updateEffectiveSorters();
}

//  qsizetype QQmlSorterCompositor::count()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QQmlSorterCompositor5countEv(
    QQmlSorterCompositor *self) {
  return self->count();
}

//  QQmlSorterBase *QQmlSorterCompositor::at(qsizetype index)
extern "C" Q_DECL_EXPORT
QQmlSorterBase *ritual_ZN20QQmlSorterCompositor2atEx(
    QQmlSorterCompositor *self,
    qsizetype index) {
  return self->at(index);
}

//  void QQmlSorterCompositor::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor5clearEv(QQmlSorterCompositor *self) {
  self->clear();
}

//  void QQmlSorterCompositor::updateCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor11updateCacheEv(
    QQmlSorterCompositor *self) {
  self->updateCache();
}

//  QQmlSorterCompositorPrivate *QQmlSorterCompositor::d_func()
extern "C" Q_DECL_EXPORT
QQmlSorterCompositorPrivate *ritual_ZN20QQmlSorterCompositor6d_funcEv(
    QQmlSorterCompositor *self) {
  return self->d_func();
}

//  const QQmlSorterCompositorPrivate *QQmlSorterCompositor::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSorterCompositorPrivate *ritual_ZNK20QQmlSorterCompositor6d_funcEv(
    const QQmlSorterCompositor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlSorterCompositor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSorterCompositor(
    QQmlSorterCompositor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSorterCompositor *>(self)->take(key, call);
}

//  QPartialOrdering QQmlSorterCompositor::compare(const QModelIndex &a0,
//      const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_own_ZNK20QQmlSorterCompositor7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlSorterCompositor *self,
    const QModelIndex *a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return new QPartialOrdering(
      self->QQmlSorterCompositor::compare(
          *a0,
          *a1,
          a2));
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
