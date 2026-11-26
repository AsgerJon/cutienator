//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQmlSorterCompositor' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 5 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsorterbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qcompare.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQmlModels/private/qqmlsortercompositor_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQmlModels__QQmlSorterCompositor.cpp, line 1, as moc:QQmlSorterCompositor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QQmlSorterCompositorE_t {};
} // unnamed namespace

template <> constexpr inline auto QQmlSorterCompositor::qt_create_metaobjectdata<qt_meta_tag_ZN20QQmlSorterCompositorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQmlSorterCompositor",
        "QML.Element",
        "anonymous",
        "QML.AddedInVersion",
        "1546",
        "updateCache",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'updateCache'
        QtMocHelpers::SlotData<void()>(5, 6, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQmlSorterCompositor, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQmlSorterCompositor::staticMetaObject = { {
    QMetaObject::SuperData::link<QQmlSorterBase::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQmlSorterCompositorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQmlSorterCompositorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QQmlSorterCompositorE_t>.metaTypes,
    nullptr
} };

void QQmlSorterCompositor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQmlSorterCompositor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->updateCache(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QQmlSorterCompositor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQmlSorterCompositor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQmlSorterCompositorE_t>.strings))
        return static_cast<void*>(this);
    return QQmlSorterBase::qt_metacast(_clname);
}

int QQmlSorterCompositor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQmlSorterBase::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

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

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 25, as _ZN20QQmlSorterCompositorD0Ev
inline QQmlSorterCompositor::~QQmlSorterCompositor()
{

}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 30, as _ZN27QQmlSorterCompositorPrivate4initEv
inline void QQmlSorterCompositorPrivate::init()
{
    Q_Q(QQmlSorterCompositor);
    m_sfpmModel = qobject_cast<QQmlSortFilterProxyModel *>(q->parent());
}

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

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 11, as _ZN20QQmlSorterCompositorC1EP7QObject
inline QQmlSorterCompositor::QQmlSorterCompositor(QObject *parent)
    : QQmlSorterBase(new QQmlSorterCompositorPrivate, parent)
{
    Q_D(QQmlSorterCompositor);
    d->init();
    // Connect the model reset with the update in the filter
    // The cache need to be updated once the model is reset with the
    // source model data.
    connect(d->m_sfpmModel, &QQmlSortFilterProxyModel::modelReset,
            this, &QQmlSorterCompositor::updateSorters);
    connect(d->m_sfpmModel, &QQmlSortFilterProxyModel::primarySorterChanged,
            this, &QQmlSorterCompositor::updateEffectiveSorters);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 109, as _ZN20QQmlSorterCompositor7sortersEv
inline QList<QQmlSorterBase *> QQmlSorterCompositor::sorters()
{
    Q_D(QQmlSorterCompositor);
    return d->m_sorters;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 115, as _ZN20QQmlSorterCompositor19sortersListPropertyEv
inline QQmlListProperty<QQmlSorterBase> QQmlSorterCompositor::sortersListProperty()
{
    Q_D(QQmlSorterCompositor);
    return QQmlListProperty<QQmlSorterBase>(reinterpret_cast<QObject*>(this), &d->m_sorters,
                                                  QQmlSorterCompositor::append,
                                                  QQmlSorterCompositor::count,
                                                  QQmlSorterCompositor::at,
                                                  QQmlSorterCompositor::clear);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 36, as _ZN20QQmlSorterCompositor6appendEP16QQmlListPropertyI14QQmlSorterBaseEPS1_
inline void QQmlSorterCompositor::append(QQmlListProperty<QQmlSorterBase> *sorterComp, QQmlSorterBase* sorter)
{
    auto *sorterCompositor = reinterpret_cast<QQmlSorterCompositor *>(sorterComp->object);
    sorterCompositor->append(sorter);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 42, as _ZN20QQmlSorterCompositor5countEP16QQmlListPropertyI14QQmlSorterBaseE
inline qsizetype QQmlSorterCompositor::count(QQmlListProperty<QQmlSorterBase> *sorterComp)
{
    auto *sorterCompositor = reinterpret_cast<QQmlSorterCompositor *> (sorterComp->object);
    return sorterCompositor->count();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 48, as _ZN20QQmlSorterCompositor2atEP16QQmlListPropertyI14QQmlSorterBaseEx
inline QQmlSorterBase *QQmlSorterCompositor::at(QQmlListProperty<QQmlSorterBase> *sorterComp, qsizetype index)
{
    auto *sorterCompositor = reinterpret_cast<QQmlSorterCompositor *> (sorterComp->object);
    return sorterCompositor->at(index);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 54, as _ZN20QQmlSorterCompositor5clearEP16QQmlListPropertyI14QQmlSorterBaseE
inline void QQmlSorterCompositor::clear(QQmlListProperty<QQmlSorterBase> *sorterComp)
{
    auto *sorterCompositor = reinterpret_cast<QQmlSorterCompositor *> (sorterComp->object);
    sorterCompositor->clear();
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

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 60, as _ZN20QQmlSorterCompositor6appendEP14QQmlSorterBase
inline void QQmlSorterCompositor::append(QQmlSorterBase *sorter)
{
    if (!sorter)
        return;
    Q_D(QQmlSorterCompositor);
    d->m_sorters.append(sorter);
    // Update sorter cache depending on the priority
    updateCache();
    // Connect the sorter to the corresponding slot to invalidate the model
    // and the sorter cache
    QObject::connect(sorter, &QQmlSorterBase::invalidateModel,
                         d->m_sfpmModel, &QQmlSortFilterProxyModel::invalidate);
    // This is needed as its required to update cache when there is any
    // change in the filter itself (for instance, a change in the priority of
    // the filter)
    QObject::connect(sorter, &QQmlSorterBase::invalidateCache,
                     this, &QQmlSorterCompositor::updateCache);
    // Reset the primary sort column when any sort order or column
    // changed
    QObject::connect(sorter, &QQmlSorterBase::sortOrderChanged,
                     this, [d] { d->resetPrimarySorter(); });
    QObject::connect(sorter, &QQmlSorterBase::columnChanged,
                     this, [d] { d->resetPrimarySorter(); });
    // Since we added new filter to the list, emit the filter changed signal
    // for the filters thats been appended to the list
    emit d->m_sfpmModel->sortersChanged();
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

//  void *QQmlSorterCompositor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQmlSorterCompositor11qt_metacastEPKc(
    QQmlSorterCompositor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlSorterCompositor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQmlSorterCompositor11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlSorterCompositor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlSorterCompositor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlSorterCompositor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSorterCompositor::tr(s, c, n));
}

//  void QQmlSorterCompositor::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor22qt_qmlMarker_anonymousEv(
    QQmlSorterCompositor *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlSorterCompositor::QQmlSorterCompositor(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlSorterCompositor *ritual_ZN20QQmlSorterCompositorC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlSorterCompositor(parent);
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

//  QQmlListProperty<QQmlSorterBase>
//      QQmlSorterCompositor::sortersListProperty()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQmlSorterBase> *ritual_ZN20QQmlSorterCompositor19sortersListPropertyEv(
    QQmlSorterCompositor *self) {
  return new QQmlListProperty<QQmlSorterBase>(self->sortersListProperty());
}

//  void QQmlSorterCompositor::append(QQmlListProperty<QQmlSorterBase>
//      *sorterComp, QQmlSorterBase *sorter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor6appendEP16QQmlListPropertyI14QQmlSorterBaseEPS1_(
    QQmlListProperty<QQmlSorterBase> *sorterComp,
    QQmlSorterBase *sorter) {
  QQmlSorterCompositor::append(sorterComp, sorter);
}

//  qsizetype QQmlSorterCompositor::count(QQmlListProperty<QQmlSorterBase>
//      *sorterComp)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QQmlSorterCompositor5countEP16QQmlListPropertyI14QQmlSorterBaseE(
    QQmlListProperty<QQmlSorterBase> *sorterComp) {
  return QQmlSorterCompositor::count(sorterComp);
}

//  QQmlSorterBase *QQmlSorterCompositor::at(QQmlListProperty<QQmlSorterBase>
//      *sorterComp, qsizetype index)
extern "C" Q_DECL_EXPORT
QQmlSorterBase *ritual_ZN20QQmlSorterCompositor2atEP16QQmlListPropertyI14QQmlSorterBaseEx(
    QQmlListProperty<QQmlSorterBase> *sorterComp,
    qsizetype index) {
  return QQmlSorterCompositor::at(sorterComp, index);
}

//  void QQmlSorterCompositor::clear(QQmlListProperty<QQmlSorterBase>
//      *sorterComp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor5clearEP16QQmlListPropertyI14QQmlSorterBaseE(
    QQmlListProperty<QQmlSorterBase> *sorterComp) {
  QQmlSorterCompositor::clear(sorterComp);
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

//  void QQmlSorterCompositor::append(QQmlSorterBase *sorter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSorterCompositor6appendEP14QQmlSorterBase(
    QQmlSorterCompositor *self,
    QQmlSorterBase *sorter) {
  self->append(sorter);
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
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlSorterCompositor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateCache()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateCache()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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

//  a QQmlListProperty<QQmlSorterBase> a ritual of QQmlSorterCompositor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSorterCompositor__QQmlListProperty_QQmlSorterBase(
    QQmlListProperty<QQmlSorterBase> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
