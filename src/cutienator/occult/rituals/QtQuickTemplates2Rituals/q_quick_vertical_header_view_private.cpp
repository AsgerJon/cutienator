//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickheaderview_p_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 84, as local:qquickheaderview.cpp:kRequiredProperty_headerView
static const char *kRequiredProperty_headerView = "headerView";

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 85, as local:qquickheaderview.cpp:kRequiredProperty_model
static const char *kRequiredProperty_model = "model";

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 121, as _ZN27QQuickHeaderViewBasePrivate12setModelImplERK8QVariant
inline void QQuickHeaderViewBasePrivate::setModelImpl(const QVariant &newModel)
{
    m_modelExplicitlySet = newModel.isValid();

    auto asTableModel = [](QAbstractItemModel *model) -> QAbstractItemModel* {
        if (qobject_cast<QAbstractTableModel *>(model))
            return model;

        // Since QQmlTableModel is not derived from QAbstractTableModel (QATM),
        // we have to check for this model separately. We want it to behave like
        // QATM to keep existing code working. This model is in the Labs module,
        // and we cannot link to it to make a qobject_cast. Therefore, we are checking
        // the class name.
        // TODO: When QQmlTableModel leaves Labs, change to qobject_cast?
        if (model && QByteArrayView(model->metaObject()->className()) == "QQmlTableModel")
            return model;
        return nullptr;
    };

    if (auto qabstracttablemodel = asTableModel(qaim(newModel))) {
        if (qabstracttablemodel != m_headerDataProxyModel.sourceModel()) {
            m_headerDataProxyModel.setSourceModel(qabstracttablemodel);
            assignedModel = QVariant::fromValue(std::addressof(m_headerDataProxyModel));
            scheduleRebuildTable(QQuickTableViewPrivate::RebuildOption::All);
            emit q_func()->modelChanged();
        }
        return;
    }

    m_headerDataProxyModel.setSourceModel(nullptr);
    QQuickTableViewPrivate::setModelImpl(newModel);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 185, as _ZN27QQuickHeaderViewBasePrivate12syncSyncViewEv
inline void QQuickHeaderViewBasePrivate::syncSyncView()
{
    if (assignedSyncDirection != orientation()) {
        qmlWarning(q_func()) << "Setting syncDirection other than Qt::"
                             << QVariant::fromValue(orientation()).toString()
                             << " is invalid.";
        assignedSyncDirection = orientation();
    }
    QQuickTableViewPrivate::syncSyncView();
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 284, as _ZN27QQuickHeaderViewBasePrivate14setOrientationEN2Qt11OrientationE
inline void QQuickHeaderViewBasePrivate::setOrientation(Qt::Orientation orientation)
{
    if (QQuickHeaderViewBasePrivate::orientation() == orientation)
        return;
    m_headerDataProxyModel.setOrientation(orientation);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 206, as _ZN27QQuickHeaderViewBasePrivate16initItemCallbackEiP7QObject
inline void QQuickHeaderViewBasePrivate::initItemCallback(int modelIndex, QObject *object)
{
    Q_Q(QQuickHeaderViewBase);

    QQuickTableViewPrivate::initItemCallback(modelIndex, object);

    auto item = qobject_cast<QQuickItem *>(object);
    if (!item)
        return;

    QQmlDelegateModelItem *modelItem = tableModel->getModelItem(modelIndex);

    setRequiredProperty(kRequiredProperty_headerView, QVariant::fromValue(q),
                        modelIndex, item, true);
    setRequiredProperty(kRequiredProperty_model, QVariant::fromValue(modelItem->modelObject()),
                        modelIndex, item, true);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 196, as _ZN27QQuickHeaderViewBasePrivate20selectionSourceModelEv
inline QAbstractItemModel *QQuickHeaderViewBasePrivate::selectionSourceModel()
{
    // Our proxy model shares no common model items with HeaderView.model. So
    // selections done in HeaderView cannot be represented in an ItemSelectionModel
    // that is shared with the syncView (and for the same reason, the mapping functions
    // modelIndex(cell) and cellAtIndex(index) have not been overridden either).
    // Instead, we set the internal proxy model as selection source model.
    return &m_headerDataProxyModel;
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 154, as _ZN27QQuickHeaderViewBasePrivate9syncModelEv
inline void QQuickHeaderViewBasePrivate::syncModel()
{
    if (!m_modelExplicitlySet && assignedSyncView) {
        // When no model has been explicitly set, but we have a syncView, we
        // should use the headerData() from the syncView's model as model.
        // If the model is not a QAbstractItemModel, or if it doesn't contain
        // any header data, header view will be empty.
        auto syncView_d = QQuickTableViewPrivate::get(assignedSyncView);
        auto syncViewModelAsQaim = qaim(syncView_d->assignedModel);
        if (syncViewModelAsQaim != m_headerDataProxyModel.sourceModel()) {
            m_headerDataProxyModel.setSourceModel(syncViewModelAsQaim); // can be nullptr
            assignedModel = QVariant::fromValue(std::addressof(m_headerDataProxyModel));
            emit q_func()->modelChanged();
        }
    }

    QQuickTableViewPrivate::syncModel();

    // For models that are just a list or a number, and especially not a
    // table, we transpose the view when the orientation is horizontal.
    // The model (list) will then be laid out horizontally rather than
    // vertically, which is otherwise the default.
    isTransposed = false;
    const auto aim = model->abstractItemModel();
    if (orientation() == Qt::Horizontal)
        isTransposed = !aim || aim->columnCount() == 1;

    if (m_textRole.isEmpty() && aim)
        m_textRole = QLatin1String("display");
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 87, as _ZN27QQuickHeaderViewBasePrivateC2Ev
inline QQuickHeaderViewBasePrivate::QQuickHeaderViewBasePrivate()
    : QQuickTableViewPrivate()
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 92, as _ZN27QQuickHeaderViewBasePrivateD2Ev
inline QQuickHeaderViewBasePrivate::~QQuickHeaderViewBasePrivate()
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 234, as _ZNK27QQuickHeaderViewBasePrivate14visualRowIndexEi
inline int QQuickHeaderViewBasePrivate::visualRowIndex(const int logicalIndex) const
{
    return (m_headerDataProxyModel.orientation() == Qt::Horizontal) ? logicalIndex : QQuickTableViewPrivate::visualRowIndex(logicalIndex);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 224, as _ZNK27QQuickHeaderViewBasePrivate15logicalRowIndexEi
inline int QQuickHeaderViewBasePrivate::logicalRowIndex(const int visualIndex) const
{
    return (m_headerDataProxyModel.orientation() == Qt::Horizontal) ? visualIndex : QQuickTableViewPrivate::logicalRowIndex(visualIndex);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 239, as _ZNK27QQuickHeaderViewBasePrivate17visualColumnIndexEi
inline int QQuickHeaderViewBasePrivate::visualColumnIndex(const int logicalIndex) const
{
    return (m_headerDataProxyModel.orientation() == Qt::Vertical) ? logicalIndex : QQuickTableViewPrivate::visualColumnIndex(logicalIndex);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 229, as _ZNK27QQuickHeaderViewBasePrivate18logicalColumnIndexEi
inline int QQuickHeaderViewBasePrivate::logicalColumnIndex(const int visualIndex) const
{
    return (m_headerDataProxyModel.orientation() == Qt::Vertical) ? visualIndex : QQuickTableViewPrivate::logicalColumnIndex(visualIndex);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 110, as _ZNK27QQuickHeaderViewBasePrivate9modelImplEv
inline QVariant QQuickHeaderViewBasePrivate::modelImpl() const
{
    // modelImpl is supposed to return the actual model that is
    // is used (that is, the proxy model), and not the source model.
    if (m_headerDataProxyModel.sourceModel())
        return QVariant::fromValue(&m_headerDataProxyModel);

    // If we're not using the proxy model, use the assigned model
    return QQuickTableViewPrivate::modelImpl();
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 397, as _ZN21QHeaderDataProxyModel14setOrientationEN2Qt11OrientationE
inline void QHeaderDataProxyModel::setOrientation(Qt::Orientation o)
{
    if (o == m_orientation)
        return;
    beginResetModel();
    m_orientation = o;
    endResetModel();
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 406, as _ZNK21QHeaderDataProxyModel11orientationEv
inline Qt::Orientation QHeaderDataProxyModel::orientation() const
{
    return m_orientation;
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 279, as _ZNK27QQuickHeaderViewBasePrivate11orientationEv
inline Qt::Orientation QQuickHeaderViewBasePrivate::orientation() const
{
    return m_headerDataProxyModel.orientation();
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 556, as _ZN31QQuickVerticalHeaderViewPrivateC1Ev
inline QQuickVerticalHeaderViewPrivate::QQuickVerticalHeaderViewPrivate()
{
    setOrientation(Qt::Vertical);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 561, as _ZN31QQuickVerticalHeaderViewPrivateD1Ev
inline QQuickVerticalHeaderViewPrivate::~QQuickVerticalHeaderViewPrivate() = default;
//  -----------------------------------------------------------------------

//  A QQuickVerticalHeaderViewPrivate that Python can take functions over in. Every QQuickVerticalHeaderViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQuickVerticalHeaderViewPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall1)(const void *, const QVariant *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall3)(const void *, int *);
typedef void * (*CuteQQuickVerticalHeaderViewPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall5)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall7)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall8)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall9)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall10)(const void *, const QQmlChangeSet *, bool, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall11)(const void *, int, QObject *, bool, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall15)(const void *, int *);
typedef void * (*CuteQQuickVerticalHeaderViewPrivateCall16)(const void *, int *);
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall17)(const void *, int *);
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall18)(const void *, const QPointF *, int, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall19)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall20)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall22)(const void *, int *);
typedef const QRectF * (*CuteQQuickVerticalHeaderViewPrivateCall23)(const void *, int *);
typedef const QSizeF * (*CuteQQuickVerticalHeaderViewPrivateCall24)(const void *, const QPointF *, const QSizeF *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall25)(const void *, const QRect *, const QRect *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall26)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall27)(const void *, QQuickPointerHandler *, int *);
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall28)(const void *, const QPointerEvent *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickVerticalHeaderViewPrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall32)(const void *, int, int *);
typedef qreal (*CuteQQuickVerticalHeaderViewPrivateCall33)(const void *, int *);
typedef qreal (*CuteQQuickVerticalHeaderViewPrivateCall34)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall35)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall36)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickVerticalHeaderViewPrivateCall37)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall38)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall39)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickVerticalHeaderViewPrivateCall40)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall41)(const void *, bool, int *);
typedef void * (*CuteQQuickVerticalHeaderViewPrivateCall42)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall43)(const void *, int *);
typedef void (*CuteQQuickVerticalHeaderViewPrivateCall44)(const void *, int, int *);
class CuteQQuickVerticalHeaderViewPrivate : public QQuickVerticalHeaderViewPrivate {
public:
  using QQuickVerticalHeaderViewPrivate::QQuickVerticalHeaderViewPrivate;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate9modelImplEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate9syncModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12syncSyncViewEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate20selectionSourceModelEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObjectb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12syncDelegateEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate16syncPositionViewEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable29selectionPointerHandlerTargetEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable12hasSelectionEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable14startSelectionERK7QPointF6QFlagsIN2Qt16KeyboardModifierEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable20setSelectionStartPosERK7QPointF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18setSelectionEndPosERK7QPointF")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable14clearSelectionEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18normalizeSelectionEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable18selectionRectangleEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18scrollTowardsPointERK7QPointFRK6QSizeF")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[36] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[39] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[44] = call;
      return true;
    }
    return false;
  }

  //  QVariant QQuickHeaderViewBasePrivate::modelImpl() const
  QVariant modelImpl() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall0 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall0>(taken[0]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickHeaderViewBasePrivate::modelImpl();
  }

  //  void QQuickHeaderViewBasePrivate::setModelImpl(const QVariant
  //      &newModel)
  void setModelImpl(const QVariant &newModel) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall1 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall1>(taken[1]);
      call(this, &newModel, &handled);
      if (handled) return;
    }
    QQuickHeaderViewBasePrivate::setModelImpl(newModel);
  }

  //  void QQuickHeaderViewBasePrivate::syncModel()
  void syncModel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall2 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickHeaderViewBasePrivate::syncModel();
  }

  //  void QQuickHeaderViewBasePrivate::syncSyncView()
  void syncSyncView() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall3 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickHeaderViewBasePrivate::syncSyncView();
  }

  //  QAbstractItemModel
  //      *QQuickHeaderViewBasePrivate::selectionSourceModel()
  QAbstractItemModel *selectionSourceModel() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall4 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractItemModel *>(given);
    }
    return QQuickHeaderViewBasePrivate::selectionSourceModel();
  }

  //  void QQuickHeaderViewBasePrivate::initItemCallback(int modelIndex,
  //      QObject *item)
  void initItemCallback(int modelIndex, QObject *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall5 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall5>(taken[5]);
      call(this, modelIndex, item, &handled);
      if (handled) return;
    }
    QQuickHeaderViewBasePrivate::initItemCallback(modelIndex, item);
  }

  //  void QQuickTableViewPrivate::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall6 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updatePolish();
  }

  //  void QQuickTableViewPrivate::itemCreatedCallback(int modelIndex,
  //      QObject *object)
  void itemCreatedCallback(int modelIndex, QObject *object) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall7 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall7>(taken[7]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemCreatedCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::itemPooledCallback(int modelIndex,
  //      QObject *object)
  void itemPooledCallback(int modelIndex, QObject *object) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall8 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall8>(taken[8]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemPooledCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::itemReusedCallback(int modelIndex,
  //      QObject *object)
  void itemReusedCallback(int modelIndex, QObject *object) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall9 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall9>(taken[9]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemReusedCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet
  //      &changeSet, bool reset)
  void modelUpdated(const QQmlChangeSet &changeSet, bool reset) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall10 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall10>(taken[10]);
      call(this, &changeSet, reset, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::modelUpdated(changeSet, reset);
  }

  //  void QQuickTableViewPrivate::updateItemProperties(int flatIndex,
  //      QObject *object, bool init)
  void updateItemProperties(
      int flatIndex,
      QObject *object,
      bool init) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall11 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall11>(taken[11]);
      call(this, flatIndex, object, init, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updateItemProperties(flatIndex, object, init);
  }

  //  void QQuickTableViewPrivate::syncWithPendingChanges()
  void syncWithPendingChanges() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall12 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncWithPendingChanges();
  }

  //  void QQuickTableViewPrivate::syncDelegate()
  void syncDelegate() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall13 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncDelegate();
  }

  //  void QQuickTableViewPrivate::syncDelegateModelAccess()
  void syncDelegateModelAccess() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall14 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncDelegateModelAccess();
  }

  //  void QQuickTableViewPrivate::syncPositionView()
  void syncPositionView() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall15 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncPositionView();
  }

  //  QQuickItem *QQuickTableViewPrivate::selectionPointerHandlerTarget()
  //      const
  QQuickItem *selectionPointerHandlerTarget() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall16 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickTableViewPrivate::selectionPointerHandlerTarget();
  }

  //  bool QQuickTableViewPrivate::hasSelection() const
  bool hasSelection() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall17 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::hasSelection();
  }

  //  bool QQuickTableViewPrivate::startSelection(const QPointF &pos,
  //      Qt::KeyboardModifiers modifiers)
  bool startSelection(
      const QPointF &pos,
      Qt::KeyboardModifiers modifiers) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall18 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall18>(taken[18]);
      bool given = call(this, &pos, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::startSelection(pos, modifiers);
  }

  //  void QQuickTableViewPrivate::setSelectionStartPos(const QPointF &pos)
  void setSelectionStartPos(const QPointF &pos) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall19 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall19>(taken[19]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setSelectionStartPos(pos);
  }

  //  void QQuickTableViewPrivate::setSelectionEndPos(const QPointF &pos)
  void setSelectionEndPos(const QPointF &pos) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall20 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall20>(taken[20]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setSelectionEndPos(pos);
  }

  //  void QQuickTableViewPrivate::clearSelection()
  void clearSelection() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall21 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::clearSelection();
  }

  //  void QQuickTableViewPrivate::normalizeSelection()
  void normalizeSelection() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall22 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::normalizeSelection();
  }

  //  QRectF QQuickTableViewPrivate::selectionRectangle() const
  QRectF selectionRectangle() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall23 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall23>(taken[23]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableViewPrivate::selectionRectangle();
  }

  //  QSizeF QQuickTableViewPrivate::scrollTowardsPoint(const QPointF &pos,
  //      const QSizeF &step)
  QSizeF scrollTowardsPoint(
      const QPointF &pos,
      const QSizeF &step) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall24 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall24>(taken[24]);
      const QSizeF * given = call(this, &pos, &step, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableViewPrivate::scrollTowardsPoint(pos, step);
  }

  //  void QQuickTableViewPrivate::updateSelection(const QRect
  //      &oldSelection, const QRect &newSelection)
  void updateSelection(
      const QRect &oldSelection,
      const QRect &newSelection) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall25 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall25>(taken[25]);
      call(this, &oldSelection, &newSelection, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updateSelection(oldSelection, newSelection);
  }

  //  void QQuickFlickablePrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall26 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall26>(taken[26]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickFlickablePrivate::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler
  //      *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall27 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall27>(taken[27]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickFlickablePrivate::addPointerHandler(h);
  }

  //  bool QQuickFlickablePrivate::wantsPointerEvent(const QPointerEvent
  //      *a0)
  bool wantsPointerEvent(const QPointerEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall28 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall28>(taken[28]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickFlickablePrivate::wantsPointerEvent(a0);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall29 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall29>(taken[29]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall30 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall30>(taken[30]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall31 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall32 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall32>(taken[32]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall33 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall34 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall34>(taken[34]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall35 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall36 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall37 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall37>(taken[37]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall38 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall38>(taken[38]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall39 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall39>(taken[39]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall40 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall40>(taken[40]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall41 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall41>(taken[41]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall42 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall43 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall43>(taken[43]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickVerticalHeaderViewPrivateCall44 call = reinterpret_cast<CuteQQuickVerticalHeaderViewPrivateCall44>(taken[44]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickVerticalHeaderView *QQuickVerticalHeaderViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickVerticalHeaderView *ritual_ZN31QQuickVerticalHeaderViewPrivate6q_funcEv(
    QQuickVerticalHeaderViewPrivate *self) {
  return self->q_func();
}

//  const QQuickVerticalHeaderView *QQuickVerticalHeaderViewPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickVerticalHeaderView *ritual_ZNK31QQuickVerticalHeaderViewPrivate6q_funcEv(
    const QQuickVerticalHeaderViewPrivate *self) {
  return self->q_func();
}

//  QQuickVerticalHeaderViewPrivate::QQuickVerticalHeaderViewPrivate()
extern "C" Q_DECL_EXPORT
QQuickVerticalHeaderViewPrivate *ritual_ZN31QQuickVerticalHeaderViewPrivateC1Ev() {
  return new CuteQQuickVerticalHeaderViewPrivate();
}

//  QQuickVerticalHeaderViewPrivate::~QQuickVerticalHeaderViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickVerticalHeaderViewPrivateD1Ev(
    QQuickVerticalHeaderViewPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickVerticalHeaderViewPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickVerticalHeaderViewPrivate(
    QQuickVerticalHeaderViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickVerticalHeaderViewPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_tableview)
