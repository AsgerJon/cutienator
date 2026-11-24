//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/qvariant.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicktableview_p.h"
#include "qquicktableview_p_p.h"
#include <QtCore/qdir.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qtimer.h>
#include <QtQml/private/qqmlincubator_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQmlModels/private/qqmldelegatecomponent_p.h>
#include <QtQmlModels/private/qqmldelegatemodel_p.h>
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQuick/qquickitemgrabresult.h>
#include <QtQuick/private/qquickflickable_p_p.h>
#include <QtQuick/private/qquickitemviewfxitem_p_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 3357, as _ZNK22QQuickTableViewPrivate14isColumnHiddenEi
inline bool QQuickTableViewPrivate::isColumnHidden(int column) const
{
    // A column is hidden if the width is explicit set to zero (either by
    // using a columnWidthProvider, or by overriding getColumnWidth()).
    return qFuzzyIsNull(getColumnWidth(column));
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 3364, as _ZNK22QQuickTableViewPrivate11isRowHiddenEi
inline bool QQuickTableViewPrivate::isRowHidden(int row) const
{
    // A row is hidden if the height is explicit set to zero (either by
    // using a rowHeightProvider, or by overriding getRowHeight()).
    return qFuzzyIsNull(getRowHeight(row));
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 2287, as _ZNK22QQuickTableViewPrivate16edgeToArrayIndexEN2Qt4EdgeE
inline int QQuickTableViewPrivate::edgeToArrayIndex(Qt::Edge edge) const
{
    return int(log2(float(edge)));
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 4536, as _ZN22QQuickTableViewPrivate18syncRebuildOptionsEv
inline void QQuickTableViewPrivate::syncRebuildOptions()
{
    if (!scheduledRebuildOptions)
        return;

    rebuildState = RebuildState::Begin;
    rebuildOptions = scheduledRebuildOptions;
    scheduledRebuildOptions = RebuildOption::None;

    if (loadedItems.isEmpty())
        rebuildOptions.setFlag(RebuildOption::All);

    // Some options are exclusive:
    if (rebuildOptions.testFlag(RebuildOption::All)) {
        rebuildOptions.setFlag(RebuildOption::ViewportOnly, false);
        rebuildOptions.setFlag(RebuildOption::LayoutOnly, false);
        rebuildOptions.setFlag(RebuildOption::CalculateNewContentWidth);
        rebuildOptions.setFlag(RebuildOption::CalculateNewContentHeight);
    } else if (rebuildOptions.testFlag(RebuildOption::ViewportOnly)) {
        rebuildOptions.setFlag(RebuildOption::LayoutOnly, false);
    }

    if (rebuildOptions.testFlag(RebuildOption::PositionViewAtRow))
        rebuildOptions.setFlag(RebuildOption::CalculateNewTopLeftRow, false);

    if (rebuildOptions.testFlag(RebuildOption::PositionViewAtColumn))
        rebuildOptions.setFlag(RebuildOption::CalculateNewTopLeftColumn, false);
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 1692, as _ZNK22QQuickTableViewPrivate19tableLayoutToStringEv
inline QString QQuickTableViewPrivate::tableLayoutToString() const
{
    if (loadedItems.isEmpty())
        return QLatin1String("table is empty!");
    return QString(QLatin1String("table cells: (%1,%2) -> (%3,%4), item count: %5, table rect: %6,%7 x %8,%9"))
            .arg(leftColumn()).arg(topRow())
            .arg(rightColumn()).arg(bottomRow())
            .arg(loadedItems.size())
            .arg(loadedTableOuterRect.x())
            .arg(loadedTableOuterRect.y())
            .arg(loadedTableOuterRect.width())
            .arg(loadedTableOuterRect.height());
}
//  -----------------------------------------------------------------------

//  A QQuickTableViewPrivate that Python can take functions over in. Every QQuickTableViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTableViewPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall1)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTableViewPrivateCall2)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTableViewPrivateCall3)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTableViewPrivateCall4)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTableViewPrivateCall5)(const void *, const QQmlChangeSet *, bool, int *);
typedef void (*CuteQQuickTableViewPrivateCall6)(const void *, int, QObject *, bool, int *);
typedef void (*CuteQQuickTableViewPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall9)(const void *, int *);
typedef const QVariant * (*CuteQQuickTableViewPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall11)(const void *, const QVariant *, int *);
typedef void (*CuteQQuickTableViewPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall14)(const void *, int *);
typedef void * (*CuteQQuickTableViewPrivateCall15)(const void *, int *);
typedef void * (*CuteQQuickTableViewPrivateCall16)(const void *, int *);
typedef bool (*CuteQQuickTableViewPrivateCall17)(const void *, int *);
typedef bool (*CuteQQuickTableViewPrivateCall18)(const void *, const QPointF *, int, int *);
typedef void (*CuteQQuickTableViewPrivateCall19)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickTableViewPrivateCall20)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickTableViewPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall22)(const void *, int *);
typedef const QRectF * (*CuteQQuickTableViewPrivateCall23)(const void *, int *);
typedef const QSizeF * (*CuteQQuickTableViewPrivateCall24)(const void *, const QPointF *, const QSizeF *, int *);
typedef void (*CuteQQuickTableViewPrivateCall25)(const void *, const QRect *, const QRect *, int *);
typedef int (*CuteQQuickTableViewPrivateCall26)(const void *, int, int *);
typedef int (*CuteQQuickTableViewPrivateCall27)(const void *, int, int *);
typedef int (*CuteQQuickTableViewPrivateCall28)(const void *, int, int *);
typedef int (*CuteQQuickTableViewPrivateCall29)(const void *, int, int *);
typedef void (*CuteQQuickTableViewPrivateCall30)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickTableViewPrivateCall31)(const void *, QQuickPointerHandler *, int *);
typedef bool (*CuteQQuickTableViewPrivateCall32)(const void *, const QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewPrivateCall33)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTableViewPrivateCall34)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTableViewPrivateCall35)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTableViewPrivateCall36)(const void *, int, int *);
typedef qreal (*CuteQQuickTableViewPrivateCall37)(const void *, int *);
typedef qreal (*CuteQQuickTableViewPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall39)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall40)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTableViewPrivateCall41)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickTableViewPrivateCall42)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickTableViewPrivateCall43)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTableViewPrivateCall44)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickTableViewPrivateCall45)(const void *, bool, int *);
typedef void * (*CuteQQuickTableViewPrivateCall46)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall47)(const void *, int *);
typedef void (*CuteQQuickTableViewPrivateCall48)(const void *, int, int *);
class CuteQQuickTableViewPrivate : public QQuickTableViewPrivate {
public:
  using QQuickTableViewPrivate::QQuickTableViewPrivate;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObjectb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12syncDelegateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate9modelImplEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate9syncModelEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12syncSyncViewEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate16syncPositionViewEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate20selectionSourceModelEv")) {
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
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate15logicalRowIndexEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate18logicalColumnIndexEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate14visualRowIndexEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate17visualColumnIndexEi")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[40] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[43] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[48] = call;
      return true;
    }
    return false;
  }

  //  void QQuickTableViewPrivate::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall0 call = reinterpret_cast<CuteQQuickTableViewPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updatePolish();
  }

  //  void QQuickTableViewPrivate::initItemCallback(int modelIndex, QObject
  //      *item)
  void initItemCallback(int modelIndex, QObject *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall1 call = reinterpret_cast<CuteQQuickTableViewPrivateCall1>(taken[1]);
      call(this, modelIndex, item, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::initItemCallback(modelIndex, item);
  }

  //  void QQuickTableViewPrivate::itemCreatedCallback(int modelIndex,
  //      QObject *object)
  void itemCreatedCallback(int modelIndex, QObject *object) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall2 call = reinterpret_cast<CuteQQuickTableViewPrivateCall2>(taken[2]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemCreatedCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::itemPooledCallback(int modelIndex,
  //      QObject *object)
  void itemPooledCallback(int modelIndex, QObject *object) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall3 call = reinterpret_cast<CuteQQuickTableViewPrivateCall3>(taken[3]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemPooledCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::itemReusedCallback(int modelIndex,
  //      QObject *object)
  void itemReusedCallback(int modelIndex, QObject *object) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall4 call = reinterpret_cast<CuteQQuickTableViewPrivateCall4>(taken[4]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemReusedCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet
  //      &changeSet, bool reset)
  void modelUpdated(const QQmlChangeSet &changeSet, bool reset) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall5 call = reinterpret_cast<CuteQQuickTableViewPrivateCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall6 call = reinterpret_cast<CuteQQuickTableViewPrivateCall6>(taken[6]);
      call(this, flatIndex, object, init, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updateItemProperties(flatIndex, object, init);
  }

  //  void QQuickTableViewPrivate::syncWithPendingChanges()
  void syncWithPendingChanges() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall7 call = reinterpret_cast<CuteQQuickTableViewPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncWithPendingChanges();
  }

  //  void QQuickTableViewPrivate::syncDelegate()
  void syncDelegate() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall8 call = reinterpret_cast<CuteQQuickTableViewPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncDelegate();
  }

  //  void QQuickTableViewPrivate::syncDelegateModelAccess()
  void syncDelegateModelAccess() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall9 call = reinterpret_cast<CuteQQuickTableViewPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncDelegateModelAccess();
  }

  //  QVariant QQuickTableViewPrivate::modelImpl() const
  QVariant modelImpl() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall10 call = reinterpret_cast<CuteQQuickTableViewPrivateCall10>(taken[10]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableViewPrivate::modelImpl();
  }

  //  void QQuickTableViewPrivate::setModelImpl(const QVariant &newModel)
  void setModelImpl(const QVariant &newModel) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall11 call = reinterpret_cast<CuteQQuickTableViewPrivateCall11>(taken[11]);
      call(this, &newModel, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setModelImpl(newModel);
  }

  //  void QQuickTableViewPrivate::syncModel()
  void syncModel() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall12 call = reinterpret_cast<CuteQQuickTableViewPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncModel();
  }

  //  void QQuickTableViewPrivate::syncSyncView()
  void syncSyncView() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall13 call = reinterpret_cast<CuteQQuickTableViewPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncSyncView();
  }

  //  void QQuickTableViewPrivate::syncPositionView()
  void syncPositionView() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall14 call = reinterpret_cast<CuteQQuickTableViewPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncPositionView();
  }

  //  QAbstractItemModel *QQuickTableViewPrivate::selectionSourceModel()
  QAbstractItemModel *selectionSourceModel() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall15 call = reinterpret_cast<CuteQQuickTableViewPrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractItemModel *>(given);
    }
    return QQuickTableViewPrivate::selectionSourceModel();
  }

  //  QQuickItem *QQuickTableViewPrivate::selectionPointerHandlerTarget()
  //      const
  QQuickItem *selectionPointerHandlerTarget() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall16 call = reinterpret_cast<CuteQQuickTableViewPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickTableViewPrivate::selectionPointerHandlerTarget();
  }

  //  bool QQuickTableViewPrivate::hasSelection() const
  bool hasSelection() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall17 call = reinterpret_cast<CuteQQuickTableViewPrivateCall17>(taken[17]);
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
      CuteQQuickTableViewPrivateCall18 call = reinterpret_cast<CuteQQuickTableViewPrivateCall18>(taken[18]);
      bool given = call(this, &pos, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::startSelection(pos, modifiers);
  }

  //  void QQuickTableViewPrivate::setSelectionStartPos(const QPointF &pos)
  void setSelectionStartPos(const QPointF &pos) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall19 call = reinterpret_cast<CuteQQuickTableViewPrivateCall19>(taken[19]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setSelectionStartPos(pos);
  }

  //  void QQuickTableViewPrivate::setSelectionEndPos(const QPointF &pos)
  void setSelectionEndPos(const QPointF &pos) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall20 call = reinterpret_cast<CuteQQuickTableViewPrivateCall20>(taken[20]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setSelectionEndPos(pos);
  }

  //  void QQuickTableViewPrivate::clearSelection()
  void clearSelection() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall21 call = reinterpret_cast<CuteQQuickTableViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::clearSelection();
  }

  //  void QQuickTableViewPrivate::normalizeSelection()
  void normalizeSelection() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall22 call = reinterpret_cast<CuteQQuickTableViewPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::normalizeSelection();
  }

  //  QRectF QQuickTableViewPrivate::selectionRectangle() const
  QRectF selectionRectangle() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall23 call = reinterpret_cast<CuteQQuickTableViewPrivateCall23>(taken[23]);
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
      CuteQQuickTableViewPrivateCall24 call = reinterpret_cast<CuteQQuickTableViewPrivateCall24>(taken[24]);
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
      CuteQQuickTableViewPrivateCall25 call = reinterpret_cast<CuteQQuickTableViewPrivateCall25>(taken[25]);
      call(this, &oldSelection, &newSelection, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updateSelection(oldSelection, newSelection);
  }

  //  int QQuickTableViewPrivate::logicalRowIndex(const int visualIndex)
  //      const
  int logicalRowIndex(const int visualIndex) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall26 call = reinterpret_cast<CuteQQuickTableViewPrivateCall26>(taken[26]);
      int given = call(this, visualIndex, &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::logicalRowIndex(visualIndex);
  }

  //  int QQuickTableViewPrivate::logicalColumnIndex(const int visualIndex)
  //      const
  int logicalColumnIndex(const int visualIndex) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall27 call = reinterpret_cast<CuteQQuickTableViewPrivateCall27>(taken[27]);
      int given = call(this, visualIndex, &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::logicalColumnIndex(visualIndex);
  }

  //  int QQuickTableViewPrivate::visualRowIndex(const int logicalIndex)
  //      const
  int visualRowIndex(const int logicalIndex) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall28 call = reinterpret_cast<CuteQQuickTableViewPrivateCall28>(taken[28]);
      int given = call(this, logicalIndex, &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::visualRowIndex(logicalIndex);
  }

  //  int QQuickTableViewPrivate::visualColumnIndex(const int logicalIndex)
  //      const
  int visualColumnIndex(const int logicalIndex) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall29 call = reinterpret_cast<CuteQQuickTableViewPrivateCall29>(taken[29]);
      int given = call(this, logicalIndex, &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::visualColumnIndex(logicalIndex);
  }

  //  void QQuickFlickablePrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall30 call = reinterpret_cast<CuteQQuickTableViewPrivateCall30>(taken[30]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickFlickablePrivate::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler
  //      *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall31 call = reinterpret_cast<CuteQQuickTableViewPrivateCall31>(taken[31]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickFlickablePrivate::addPointerHandler(h);
  }

  //  bool QQuickFlickablePrivate::wantsPointerEvent(const QPointerEvent
  //      *a0)
  bool wantsPointerEvent(const QPointerEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall32 call = reinterpret_cast<CuteQQuickTableViewPrivateCall32>(taken[32]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickFlickablePrivate::wantsPointerEvent(a0);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall33 call = reinterpret_cast<CuteQQuickTableViewPrivateCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall34 call = reinterpret_cast<CuteQQuickTableViewPrivateCall34>(taken[34]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall35 call = reinterpret_cast<CuteQQuickTableViewPrivateCall35>(taken[35]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall36 call = reinterpret_cast<CuteQQuickTableViewPrivateCall36>(taken[36]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall37 call = reinterpret_cast<CuteQQuickTableViewPrivateCall37>(taken[37]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall38 call = reinterpret_cast<CuteQQuickTableViewPrivateCall38>(taken[38]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall39 call = reinterpret_cast<CuteQQuickTableViewPrivateCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall40 call = reinterpret_cast<CuteQQuickTableViewPrivateCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall41 call = reinterpret_cast<CuteQQuickTableViewPrivateCall41>(taken[41]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall42 call = reinterpret_cast<CuteQQuickTableViewPrivateCall42>(taken[42]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall43 call = reinterpret_cast<CuteQQuickTableViewPrivateCall43>(taken[43]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall44 call = reinterpret_cast<CuteQQuickTableViewPrivateCall44>(taken[44]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall45 call = reinterpret_cast<CuteQQuickTableViewPrivateCall45>(taken[45]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall46 call = reinterpret_cast<CuteQQuickTableViewPrivateCall46>(taken[46]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall47 call = reinterpret_cast<CuteQQuickTableViewPrivateCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickTableViewPrivateCall48 call = reinterpret_cast<CuteQQuickTableViewPrivateCall48>(taken[48]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickTableView *QQuickTableViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTableView *ritual_ZN22QQuickTableViewPrivate6q_funcEv(
    QQuickTableViewPrivate *self) {
  return self->q_func();
}

//  const QQuickTableView *QQuickTableViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTableView *ritual_ZNK22QQuickTableViewPrivate6q_funcEv(
    const QQuickTableViewPrivate *self) {
  return self->q_func();
}

//  QQuickTableViewPrivate::QQuickTableViewPrivate()
extern "C" Q_DECL_EXPORT
QQuickTableViewPrivate *ritual_ZN22QQuickTableViewPrivateC1Ev() {
  return new CuteQQuickTableViewPrivate();
}

//  QQuickTableViewPrivate::~QQuickTableViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivateD1Ev(QQuickTableViewPrivate *self) {
  delete self;
}

//  QQuickTableViewPrivate *QQuickTableViewPrivate::get(QQuickTableView *q)
extern "C" Q_DECL_EXPORT
QQuickTableViewPrivate *ritual_ZN22QQuickTableViewPrivate3getEP15QQuickTableView(
    QQuickTableView *q) {
  return QQuickTableViewPrivate::get(q);
}

//  void QQuickTableViewPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12updatePolishEv(
    QQuickTableViewPrivate *self) {
  self->updatePolish();
}

//  void QQuickTableViewPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate4initEv(QQuickTableViewPrivate *self) {
  self->init();
}

//  QQuickTableViewAttached *QQuickTableViewPrivate::getAttachedObject(const
//      QObject *object) const
extern "C" Q_DECL_EXPORT
QQuickTableViewAttached *ritual_ZNK22QQuickTableViewPrivate17getAttachedObjectEPK7QObject(
    const QQuickTableViewPrivate *self,
    const QObject *object) {
  return self->getAttachedObject(object);
}

//  int QQuickTableViewPrivate::modelIndexAtCell(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate16modelIndexAtCellERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->modelIndexAtCell(*cell);
}

//  QPoint QQuickTableViewPrivate::cellAtModelIndex(int modelIndex) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK22QQuickTableViewPrivate16cellAtModelIndexEi(
    const QQuickTableViewPrivate *self,
    int modelIndex) {
  return new QPoint(self->cellAtModelIndex(modelIndex));
}

//  int QQuickTableViewPrivate::modelIndexToCellIndex(const QModelIndex
//      &modelIndex, bool visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate21modelIndexToCellIndexERK11QModelIndexb(
    const QQuickTableViewPrivate *self,
    const QModelIndex *modelIndex,
    bool visualIndex) {
  return self->modelIndexToCellIndex(*modelIndex, visualIndex);
}

//  bool QQuickTableViewPrivate::cellIsValid(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate11cellIsValidERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->cellIsValid(*cell);
}

//  qreal QQuickTableViewPrivate::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate17sizeHintForColumnEi(
    const QQuickTableViewPrivate *self,
    int column) {
  return self->sizeHintForColumn(column);
}

//  qreal QQuickTableViewPrivate::sizeHintForRow(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate14sizeHintForRowEi(
    const QQuickTableViewPrivate *self,
    int row) {
  return self->sizeHintForRow(row);
}

//  QSize QQuickTableViewPrivate::calculateTableSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN22QQuickTableViewPrivate18calculateTableSizeEv(
    QQuickTableViewPrivate *self) {
  return new QSize(self->calculateTableSize());
}

//  bool QQuickTableViewPrivate::isColumnHidden(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate14isColumnHiddenEi(
    const QQuickTableViewPrivate *self,
    int column) {
  return self->isColumnHidden(column);
}

//  bool QQuickTableViewPrivate::isRowHidden(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate11isRowHiddenEi(
    const QQuickTableViewPrivate *self,
    int row) {
  return self->isRowHidden(row);
}

//  qreal QQuickTableViewPrivate::getColumnLayoutWidth(int column)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN22QQuickTableViewPrivate20getColumnLayoutWidthEi(
    QQuickTableViewPrivate *self,
    int column) {
  return self->getColumnLayoutWidth(column);
}

//  qreal QQuickTableViewPrivate::getRowLayoutHeight(int row)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN22QQuickTableViewPrivate18getRowLayoutHeightEi(
    QQuickTableViewPrivate *self,
    int row) {
  return self->getRowLayoutHeight(row);
}

//  qreal QQuickTableViewPrivate::getColumnWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate14getColumnWidthEi(
    const QQuickTableViewPrivate *self,
    int column) {
  return self->getColumnWidth(column);
}

//  qreal QQuickTableViewPrivate::getRowHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate12getRowHeightEi(
    const QQuickTableViewPrivate *self,
    int row) {
  return self->getRowHeight(row);
}

//  qreal QQuickTableViewPrivate::getEffectiveRowY(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate16getEffectiveRowYEi(
    const QQuickTableViewPrivate *self,
    int row) {
  return self->getEffectiveRowY(row);
}

//  qreal QQuickTableViewPrivate::getEffectiveRowHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate21getEffectiveRowHeightEi(
    const QQuickTableViewPrivate *self,
    int row) {
  return self->getEffectiveRowHeight(row);
}

//  qreal QQuickTableViewPrivate::getEffectiveColumnX(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate19getEffectiveColumnXEi(
    const QQuickTableViewPrivate *self,
    int column) {
  return self->getEffectiveColumnX(column);
}

//  qreal QQuickTableViewPrivate::getEffectiveColumnWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate23getEffectiveColumnWidthEi(
    const QQuickTableViewPrivate *self,
    int column) {
  return self->getEffectiveColumnWidth(column);
}

//  qreal QQuickTableViewPrivate::getAlignmentContentX(int column,
//      Qt::Alignment alignment, const qreal offset, const QRectF &subRect)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN22QQuickTableViewPrivate20getAlignmentContentXEi6QFlagsIN2Qt13AlignmentFlagEEdRK6QRectF(
    QQuickTableViewPrivate *self,
    int column,
    int alignment,
    qreal offset,
    const QRectF *subRect) {
  return self->getAlignmentContentX(
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      offset,
      *subRect);
}

//  qreal QQuickTableViewPrivate::getAlignmentContentY(int row, Qt::Alignment
//      alignment, const qreal offset, const QRectF &subRect)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN22QQuickTableViewPrivate20getAlignmentContentYEi6QFlagsIN2Qt13AlignmentFlagEEdRK6QRectF(
    QQuickTableViewPrivate *self,
    int row,
    int alignment,
    qreal offset,
    const QRectF *subRect) {
  return self->getAlignmentContentY(
      row,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      offset,
      *subRect);
}

//  int QQuickTableViewPrivate::topRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate6topRowEv(
    const QQuickTableViewPrivate *self) {
  return self->topRow();
}

//  int QQuickTableViewPrivate::bottomRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate9bottomRowEv(
    const QQuickTableViewPrivate *self) {
  return self->bottomRow();
}

//  int QQuickTableViewPrivate::leftColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate10leftColumnEv(
    const QQuickTableViewPrivate *self) {
  return self->leftColumn();
}

//  int QQuickTableViewPrivate::rightColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate11rightColumnEv(
    const QQuickTableViewPrivate *self) {
  return self->rightColumn();
}

//  QQuickTableView *QQuickTableViewPrivate::rootSyncView() const
extern "C" Q_DECL_EXPORT
QQuickTableView *ritual_ZNK22QQuickTableViewPrivate12rootSyncViewEv(
    const QQuickTableViewPrivate *self) {
  return self->rootSyncView();
}

//  bool QQuickTableViewPrivate::updateTableRecursive()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate20updateTableRecursiveEv(
    QQuickTableViewPrivate *self) {
  return self->updateTableRecursive();
}

//  bool QQuickTableViewPrivate::updateTable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate11updateTableEv(
    QQuickTableViewPrivate *self) {
  return self->updateTable();
}

//  void QQuickTableViewPrivate::relayoutTableItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18relayoutTableItemsEv(
    QQuickTableViewPrivate *self) {
  self->relayoutTableItems();
}

//  void QQuickTableViewPrivate::layoutVerticalEdge(Qt::Edge tableEdge)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18layoutVerticalEdgeEN2Qt4EdgeE(
    QQuickTableViewPrivate *self,
    Qt::Edge tableEdge) {
  self->layoutVerticalEdge(tableEdge);
}

//  void QQuickTableViewPrivate::layoutHorizontalEdge(Qt::Edge tableEdge)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20layoutHorizontalEdgeEN2Qt4EdgeE(
    QQuickTableViewPrivate *self,
    Qt::Edge tableEdge) {
  self->layoutHorizontalEdge(tableEdge);
}

//  void QQuickTableViewPrivate::layoutTopLeftItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17layoutTopLeftItemEv(
    QQuickTableViewPrivate *self) {
  self->layoutTopLeftItem();
}

//  void QQuickTableViewPrivate::layoutTableEdgeFromLoadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate30layoutTableEdgeFromLoadRequestEv(
    QQuickTableViewPrivate *self) {
  self->layoutTableEdgeFromLoadRequest();
}

//  void QQuickTableViewPrivate::updateContentWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18updateContentWidthEv(
    QQuickTableViewPrivate *self) {
  self->updateContentWidth();
}

//  void QQuickTableViewPrivate::updateContentHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate19updateContentHeightEv(
    QQuickTableViewPrivate *self) {
  self->updateContentHeight();
}

//  void QQuickTableViewPrivate::updateAverageColumnWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate24updateAverageColumnWidthEv(
    QQuickTableViewPrivate *self) {
  self->updateAverageColumnWidth();
}

//  void QQuickTableViewPrivate::updateAverageRowHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate22updateAverageRowHeightEv(
    QQuickTableViewPrivate *self) {
  self->updateAverageRowHeight();
}

//  RebuildOptions QQuickTableViewPrivate::checkForVisibilityChanges()
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickTableViewPrivate25checkForVisibilityChangesEv(
    QQuickTableViewPrivate *self) {
  return static_cast<int>(self->checkForVisibilityChanges().toInt());
}

//  void QQuickTableViewPrivate::forceLayout(bool immediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate11forceLayoutEb(
    QQuickTableViewPrivate *self,
    bool immediate) {
  self->forceLayout(immediate);
}

//  void QQuickTableViewPrivate::updateExtents()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate13updateExtentsEv(
    QQuickTableViewPrivate *self) {
  self->updateExtents();
}

//  void QQuickTableViewPrivate::syncLoadedTableRectFromLoadedTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate34syncLoadedTableRectFromLoadedTableEv(
    QQuickTableViewPrivate *self) {
  self->syncLoadedTableRectFromLoadedTable();
}

//  void QQuickTableViewPrivate::syncLoadedTableFromLoadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate30syncLoadedTableFromLoadRequestEv(
    QQuickTableViewPrivate *self) {
  self->syncLoadedTableFromLoadRequest();
}

//  int QQuickTableViewPrivate::nextVisibleEdgeIndex(Qt::Edge edge, int
//      startIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate20nextVisibleEdgeIndexEN2Qt4EdgeEi(
    const QQuickTableViewPrivate *self,
    Qt::Edge edge,
    int startIndex) {
  return self->nextVisibleEdgeIndex(edge, startIndex);
}

//  int
//      QQuickTableViewPrivate::nextVisibleEdgeIndexAroundLoadedTable(Qt::Edg
//      e edge) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate37nextVisibleEdgeIndexAroundLoadedTableEN2Qt4EdgeE(
    const QQuickTableViewPrivate *self,
    Qt::Edge edge) {
  return self->nextVisibleEdgeIndexAroundLoadedTable(edge);
}

//  bool QQuickTableViewPrivate::atTableEnd(Qt::Edge edge) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate10atTableEndEN2Qt4EdgeE(
    const QQuickTableViewPrivate *self,
    Qt::Edge edge) {
  return self->atTableEnd(edge);
}

//  bool QQuickTableViewPrivate::atTableEnd(Qt::Edge edge, int startIndex)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate10atTableEndEN2Qt4EdgeEi(
    const QQuickTableViewPrivate *self,
    Qt::Edge edge,
    int startIndex) {
  return self->atTableEnd(edge, startIndex);
}

//  int QQuickTableViewPrivate::edgeToArrayIndex(Qt::Edge edge) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate16edgeToArrayIndexEN2Qt4EdgeE(
    const QQuickTableViewPrivate *self,
    Qt::Edge edge) {
  return self->edgeToArrayIndex(edge);
}

//  void QQuickTableViewPrivate::clearEdgeSizeCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18clearEdgeSizeCacheEv(
    QQuickTableViewPrivate *self) {
  self->clearEdgeSizeCache();
}

//  bool QQuickTableViewPrivate::canLoadTableEdge(Qt::Edge tableEdge, const
//      QRectF fillRect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate16canLoadTableEdgeEN2Qt4EdgeE6QRectF(
    const QQuickTableViewPrivate *self,
    Qt::Edge tableEdge,
    const QRectF *fillRect) {
  return self->canLoadTableEdge(tableEdge, *fillRect);
}

//  bool QQuickTableViewPrivate::canUnloadTableEdge(Qt::Edge tableEdge, const
//      QRectF fillRect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate18canUnloadTableEdgeEN2Qt4EdgeE6QRectF(
    const QQuickTableViewPrivate *self,
    Qt::Edge tableEdge,
    const QRectF *fillRect) {
  return self->canUnloadTableEdge(tableEdge, *fillRect);
}

//  Qt::Edge QQuickTableViewPrivate::nextEdgeToLoad(const QRectF rect)
extern "C" Q_DECL_EXPORT
Qt::Edge ritual_ZN22QQuickTableViewPrivate14nextEdgeToLoadE6QRectF(
    QQuickTableViewPrivate *self,
    const QRectF *rect) {
  return self->nextEdgeToLoad(*rect);
}

//  Qt::Edge QQuickTableViewPrivate::nextEdgeToUnload(const QRectF rect)
extern "C" Q_DECL_EXPORT
Qt::Edge ritual_ZN22QQuickTableViewPrivate16nextEdgeToUnloadE6QRectF(
    QQuickTableViewPrivate *self,
    const QRectF *rect) {
  return self->nextEdgeToUnload(*rect);
}

//  qreal QQuickTableViewPrivate::cellWidth(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate9cellWidthERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->cellWidth(*cell);
}

//  qreal QQuickTableViewPrivate::cellHeight(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTableViewPrivate10cellHeightERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->cellHeight(*cell);
}

//  FxTableItem *QQuickTableViewPrivate::loadedTableItem(const QPoint &cell)
//      const
extern "C" Q_DECL_EXPORT
FxTableItem *ritual_ZNK22QQuickTableViewPrivate15loadedTableItemERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->loadedTableItem(*cell);
}

//  FxTableItem *QQuickTableViewPrivate::createFxTableItem(const QPoint
//      &cell, QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
FxTableItem *ritual_ZN22QQuickTableViewPrivate17createFxTableItemERK6QPointN13QQmlIncubator14IncubationModeE(
    QQuickTableViewPrivate *self,
    const QPoint *cell,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->createFxTableItem(*cell, incubationMode);
}

//  FxTableItem *QQuickTableViewPrivate::loadFxTableItem(const QPoint &cell,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
FxTableItem *ritual_ZN22QQuickTableViewPrivate15loadFxTableItemERK6QPointN13QQmlIncubator14IncubationModeE(
    QQuickTableViewPrivate *self,
    const QPoint *cell,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->loadFxTableItem(*cell, incubationMode);
}

//  void QQuickTableViewPrivate::unloadItem(const QPoint &cell)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate10unloadItemERK6QPoint(
    QQuickTableViewPrivate *self,
    const QPoint *cell) {
  self->unloadItem(*cell);
}

//  void QQuickTableViewPrivate::loadEdge(Qt::Edge edge,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate8loadEdgeEN2Qt4EdgeEN13QQmlIncubator14IncubationModeE(
    QQuickTableViewPrivate *self,
    Qt::Edge edge,
    QQmlIncubator::IncubationMode incubationMode) {
  self->loadEdge(edge, incubationMode);
}

//  void QQuickTableViewPrivate::unloadEdge(Qt::Edge edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate10unloadEdgeEN2Qt4EdgeE(
    QQuickTableViewPrivate *self,
    Qt::Edge edge) {
  self->unloadEdge(edge);
}

//  void QQuickTableViewPrivate::loadAndUnloadVisibleEdges(QQmlIncubator::Inc
//      ubationMode incubationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate25loadAndUnloadVisibleEdgesEN13QQmlIncubator14IncubationModeE(
    QQuickTableViewPrivate *self,
    QQmlIncubator::IncubationMode incubationMode) {
  self->loadAndUnloadVisibleEdges(incubationMode);
}

//  void QQuickTableViewPrivate::drainReusePoolAfterLoadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate30drainReusePoolAfterLoadRequestEv(
    QQuickTableViewPrivate *self) {
  self->drainReusePoolAfterLoadRequest();
}

//  void QQuickTableViewPrivate::processLoadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18processLoadRequestEv(
    QQuickTableViewPrivate *self) {
  self->processLoadRequest();
}

//  void QQuickTableViewPrivate::processRebuildTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate19processRebuildTableEv(
    QQuickTableViewPrivate *self) {
  self->processRebuildTable();
}

//  bool QQuickTableViewPrivate::moveToNextRebuildState()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate22moveToNextRebuildStateEv(
    QQuickTableViewPrivate *self) {
  return self->moveToNextRebuildState();
}

//  void QQuickTableViewPrivate::loadInitialTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate16loadInitialTableEv(
    QQuickTableViewPrivate *self) {
  self->loadInitialTable();
}

//  void QQuickTableViewPrivate::layoutAfterLoadingInitialTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate30layoutAfterLoadingInitialTableEv(
    QQuickTableViewPrivate *self) {
  self->layoutAfterLoadingInitialTable();
}

//  void QQuickTableViewPrivate::adjustViewportXAccordingToAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate35adjustViewportXAccordingToAlignmentEv(
    QQuickTableViewPrivate *self) {
  self->adjustViewportXAccordingToAlignment();
}

//  void QQuickTableViewPrivate::adjustViewportYAccordingToAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate35adjustViewportYAccordingToAlignmentEv(
    QQuickTableViewPrivate *self) {
  self->adjustViewportYAccordingToAlignment();
}

//  void QQuickTableViewPrivate::cancelOvershootAfterLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate26cancelOvershootAfterLayoutEv(
    QQuickTableViewPrivate *self) {
  self->cancelOvershootAfterLayout();
}

//  void QQuickTableViewPrivate::scheduleRebuildTable(QQuickTableViewPrivate:
//      :RebuildOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20scheduleRebuildTableE6QFlagsINS_13RebuildOptionEE(
    QQuickTableViewPrivate *self,
    int options) {
  self->scheduleRebuildTable(
      QFlags<QQuickTableViewPrivate::RebuildOption>::fromInt(options));
}

#if QT_CONFIG(cursor)
//  void QQuickTableViewPrivate::updateCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12updateCursorEv(
    QQuickTableViewPrivate *self) {
  self->updateCursor();
}
#endif  // QT_CONFIG(cursor)

//  void QQuickTableViewPrivate::updateEditItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate14updateEditItemEv(
    QQuickTableViewPrivate *self) {
  self->updateEditItem();
}

//  void QQuickTableViewPrivate::updateContentSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17updateContentSizeEv(
    QQuickTableViewPrivate *self) {
  self->updateContentSize();
}

//  QTypeRevision QQuickTableViewPrivate::resolveImportVersion()
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN22QQuickTableViewPrivate20resolveImportVersionEv(
    QQuickTableViewPrivate *self) {
  return new QTypeRevision(self->resolveImportVersion());
}

//  void QQuickTableViewPrivate::createWrapperModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18createWrapperModelEv(
    QQuickTableViewPrivate *self) {
  self->createWrapperModel();
}

//  QAbstractItemModel *QQuickTableViewPrivate::qaim(QVariant modelAsVariant)
//      const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK22QQuickTableViewPrivate4qaimE8QVariant(
    const QQuickTableViewPrivate *self,
    const QVariant *modelAsVariant) {
  return self->qaim(*modelAsVariant);
}

//  void QQuickTableViewPrivate::initItemCallback(int modelIndex, QObject
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *item) {
  self->initItemCallback(modelIndex, item);
}

//  void QQuickTableViewPrivate::itemCreatedCallback(int modelIndex, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *object) {
  self->itemCreatedCallback(modelIndex, object);
}

//  void QQuickTableViewPrivate::itemPooledCallback(int modelIndex, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *object) {
  self->itemPooledCallback(modelIndex, object);
}

//  void QQuickTableViewPrivate::itemReusedCallback(int modelIndex, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *object) {
  self->itemReusedCallback(modelIndex, object);
}

//  void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet &changeSet,
//      bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb(
    QQuickTableViewPrivate *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->modelUpdated(*changeSet, reset);
}

//  void QQuickTableViewPrivate::updateItemProperties(int flatIndex, QObject
//      *object, bool init)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObjectb(
    QQuickTableViewPrivate *self,
    int flatIndex,
    QObject *object,
    bool init) {
  self->updateItemProperties(flatIndex, object, init);
}

//  void QQuickTableViewPrivate::syncWithPendingChanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv(
    QQuickTableViewPrivate *self) {
  self->syncWithPendingChanges();
}

//  void QQuickTableViewPrivate::syncDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12syncDelegateEv(
    QQuickTableViewPrivate *self) {
  self->syncDelegate();
}

//  void QQuickTableViewPrivate::syncDelegateModelAccess()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv(
    QQuickTableViewPrivate *self) {
  self->syncDelegateModelAccess();
}

//  QVariant QQuickTableViewPrivate::modelImpl() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QQuickTableViewPrivate9modelImplEv(
    const QQuickTableViewPrivate *self) {
  return new QVariant(self->modelImpl());
}

//  void QQuickTableViewPrivate::setModelImpl(const QVariant &newModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant(
    QQuickTableViewPrivate *self,
    const QVariant *newModel) {
  self->setModelImpl(*newModel);
}

//  void QQuickTableViewPrivate::syncModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate9syncModelEv(
    QQuickTableViewPrivate *self) {
  self->syncModel();
}

//  void QQuickTableViewPrivate::syncSyncView()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12syncSyncViewEv(
    QQuickTableViewPrivate *self) {
  self->syncSyncView();
}

//  void QQuickTableViewPrivate::syncPositionView()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate16syncPositionViewEv(
    QQuickTableViewPrivate *self) {
  self->syncPositionView();
}

//  QAbstractItemModel *QQuickTableViewPrivate::selectionSourceModel()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN22QQuickTableViewPrivate20selectionSourceModelEv(
    QQuickTableViewPrivate *self) {
  return self->selectionSourceModel();
}

//  void QQuickTableViewPrivate::syncRebuildOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18syncRebuildOptionsEv(
    QQuickTableViewPrivate *self) {
  self->syncRebuildOptions();
}

//  void QQuickTableViewPrivate::connectToModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate14connectToModelEv(
    QQuickTableViewPrivate *self) {
  self->connectToModel();
}

//  void QQuickTableViewPrivate::disconnectFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate19disconnectFromModelEv(
    QQuickTableViewPrivate *self) {
  self->disconnectFromModel();
}

//  void QQuickTableViewPrivate::rowsMovedCallback(const QModelIndex &parent,
//      int start, int end, const QModelIndex &destination, int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17rowsMovedCallbackERK11QModelIndexiiS2_i(
    QQuickTableViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end,
    const QModelIndex *destination,
    int row) {
  self->rowsMovedCallback(*parent, start, end, *destination, row);
}

//  void QQuickTableViewPrivate::columnsMovedCallback(const QModelIndex
//      &parent, int start, int end, const QModelIndex &destination, int
//      column)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20columnsMovedCallbackERK11QModelIndexiiS2_i(
    QQuickTableViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end,
    const QModelIndex *destination,
    int column) {
  self->columnsMovedCallback(*parent, start, end, *destination, column);
}

//  void QQuickTableViewPrivate::rowsInsertedCallback(const QModelIndex
//      &parent, int begin, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20rowsInsertedCallbackERK11QModelIndexii(
    QQuickTableViewPrivate *self,
    const QModelIndex *parent,
    int begin,
    int end) {
  self->rowsInsertedCallback(*parent, begin, end);
}

//  void QQuickTableViewPrivate::rowsRemovedCallback(const QModelIndex
//      &parent, int begin, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate19rowsRemovedCallbackERK11QModelIndexii(
    QQuickTableViewPrivate *self,
    const QModelIndex *parent,
    int begin,
    int end) {
  self->rowsRemovedCallback(*parent, begin, end);
}

//  void QQuickTableViewPrivate::columnsInsertedCallback(const QModelIndex
//      &parent, int begin, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate23columnsInsertedCallbackERK11QModelIndexii(
    QQuickTableViewPrivate *self,
    const QModelIndex *parent,
    int begin,
    int end) {
  self->columnsInsertedCallback(*parent, begin, end);
}

//  void QQuickTableViewPrivate::columnsRemovedCallback(const QModelIndex
//      &parent, int begin, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate22columnsRemovedCallbackERK11QModelIndexii(
    QQuickTableViewPrivate *self,
    const QModelIndex *parent,
    int begin,
    int end) {
  self->columnsRemovedCallback(*parent, begin, end);
}

//  void QQuickTableViewPrivate::layoutChangedCallback(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate21layoutChangedCallbackERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QQuickTableViewPrivate *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->layoutChangedCallback(*parents, hint);
}

//  void QQuickTableViewPrivate::modelResetCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18modelResetCallbackEv(
    QQuickTableViewPrivate *self) {
  self->modelResetCallback();
}

//  void QQuickTableViewPrivate::positionViewAtRow(int row, Qt::Alignment
//      alignment, qreal offset, const QRectF subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17positionViewAtRowEi6QFlagsIN2Qt13AlignmentFlagEEd6QRectF(
    QQuickTableViewPrivate *self,
    int row,
    int alignment,
    qreal offset,
    const QRectF *subRect) {
  self->positionViewAtRow(
      row,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      offset,
      *subRect);
}

//  void QQuickTableViewPrivate::positionViewAtColumn(int column,
//      Qt::Alignment alignment, qreal offset, const QRectF subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20positionViewAtColumnEi6QFlagsIN2Qt13AlignmentFlagEEd6QRectF(
    QQuickTableViewPrivate *self,
    int column,
    int alignment,
    qreal offset,
    const QRectF *subRect) {
  self->positionViewAtColumn(
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      offset,
      *subRect);
}

//  bool QQuickTableViewPrivate::scrollToRow(int row, Qt::Alignment
//      alignment, qreal offset, const QRectF subRect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate11scrollToRowEi6QFlagsIN2Qt13AlignmentFlagEEd6QRectF(
    QQuickTableViewPrivate *self,
    int row,
    int alignment,
    qreal offset,
    const QRectF *subRect) {
  return self->scrollToRow(
      row,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      offset,
      *subRect);
}

//  bool QQuickTableViewPrivate::scrollToColumn(int column, Qt::Alignment
//      alignment, qreal offset, const QRectF subRect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate14scrollToColumnEi6QFlagsIN2Qt13AlignmentFlagEEd6QRectF(
    QQuickTableViewPrivate *self,
    int column,
    int alignment,
    qreal offset,
    const QRectF *subRect) {
  return self->scrollToColumn(
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      offset,
      *subRect);
}

//  void QQuickTableViewPrivate::scheduleRebuildIfFastFlick()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate26scheduleRebuildIfFastFlickEv(
    QQuickTableViewPrivate *self) {
  self->scheduleRebuildIfFastFlick();
}

//  void QQuickTableViewPrivate::setLocalViewportX(qreal contentX)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17setLocalViewportXEd(
    QQuickTableViewPrivate *self,
    qreal contentX) {
  self->setLocalViewportX(contentX);
}

//  void QQuickTableViewPrivate::setLocalViewportY(qreal contentY)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17setLocalViewportYEd(
    QQuickTableViewPrivate *self,
    qreal contentY) {
  self->setLocalViewportY(contentY);
}

//  void QQuickTableViewPrivate::syncViewportRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate16syncViewportRectEv(
    QQuickTableViewPrivate *self) {
  self->syncViewportRect();
}

//  void QQuickTableViewPrivate::syncViewportPosRecursive()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate24syncViewportPosRecursiveEv(
    QQuickTableViewPrivate *self) {
  self->syncViewportPosRecursive();
}

//  bool QQuickTableViewPrivate::selectedInSelectionModel(const QPoint &cell)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate24selectedInSelectionModelERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->selectedInSelectionModel(*cell);
}

//  void QQuickTableViewPrivate::selectionChangedInSelectionModel(const
//      QItemSelection &selected, const QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate32selectionChangedInSelectionModelERK14QItemSelectionS2_(
    QQuickTableViewPrivate *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  self->selectionChangedInSelectionModel(*selected, *deselected);
}

//  void QQuickTableViewPrivate::updateSelectedOnAllDelegateItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate32updateSelectedOnAllDelegateItemsEv(
    QQuickTableViewPrivate *self) {
  self->updateSelectedOnAllDelegateItems();
}

//  void QQuickTableViewPrivate::setSelectedOnDelegateItem(const QModelIndex
//      &modelIndex, bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate25setSelectedOnDelegateItemERK11QModelIndexb(
    QQuickTableViewPrivate *self,
    const QModelIndex *modelIndex,
    bool select) {
  self->setSelectedOnDelegateItem(*modelIndex, select);
}

//  bool QQuickTableViewPrivate::currentInSelectionModel(const QPoint &cell)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate23currentInSelectionModelERK6QPoint(
    const QQuickTableViewPrivate *self,
    const QPoint *cell) {
  return self->currentInSelectionModel(*cell);
}

//  void QQuickTableViewPrivate::currentChangedInSelectionModel(const
//      QModelIndex &current, const QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate30currentChangedInSelectionModelERK11QModelIndexS2_(
    QQuickTableViewPrivate *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  self->currentChangedInSelectionModel(*current, *previous);
}

//  void QQuickTableViewPrivate::setCurrentOnDelegateItem(const QModelIndex
//      &index, bool isCurrent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate24setCurrentOnDelegateItemERK11QModelIndexb(
    QQuickTableViewPrivate *self,
    const QModelIndex *index,
    bool isCurrent) {
  self->setCurrentOnDelegateItem(*index, isCurrent);
}

//  void QQuickTableViewPrivate::updateCurrentRowAndColumn()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate25updateCurrentRowAndColumnEv(
    QQuickTableViewPrivate *self) {
  self->updateCurrentRowAndColumn();
}

//  void QQuickTableViewPrivate::fetchMoreData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate13fetchMoreDataEv(
    QQuickTableViewPrivate *self) {
  self->fetchMoreData();
}

//  QString QQuickTableViewPrivate::tableLayoutToString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTableViewPrivate19tableLayoutToStringEv(
    const QQuickTableViewPrivate *self) {
  return new QString(self->tableLayoutToString());
}

//  void QQuickTableViewPrivate::dumpTable() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickTableViewPrivate9dumpTableEv(
    const QQuickTableViewPrivate *self) {
  self->dumpTable();
}

//  void QQuickTableViewPrivate::setRequiredProperty(const char *property,
//      const QVariant &value, int serializedModelIndex, QObject *object,
//      bool init)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate19setRequiredPropertyEPKcRK8QVariantiP7QObjectb(
    QQuickTableViewPrivate *self,
    const char *property,
    const QVariant *value,
    int serializedModelIndex,
    QObject *object,
    bool init) {
  self->setRequiredProperty(
      property,
      *value,
      serializedModelIndex,
      object,
      init);
}

//  void QQuickTableViewPrivate::handleTap(const QQuickHandlerPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate9handleTapERK18QQuickHandlerPoint(
    QQuickTableViewPrivate *self,
    const QQuickHandlerPoint *point) {
  self->handleTap(*point);
}

//  void QQuickTableViewPrivate::setCurrentIndexFromTap(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate22setCurrentIndexFromTapERK7QPointF(
    QQuickTableViewPrivate *self,
    const QPointF *pos) {
  self->setCurrentIndexFromTap(*pos);
}

//  void QQuickTableViewPrivate::setCurrentIndex(const QPoint &cell)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate15setCurrentIndexERK6QPoint(
    QQuickTableViewPrivate *self,
    const QPoint *cell) {
  self->setCurrentIndex(*cell);
}

//  bool QQuickTableViewPrivate::setCurrentIndexFromKeyEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate27setCurrentIndexFromKeyEventEP9QKeyEvent(
    QQuickTableViewPrivate *self,
    QKeyEvent *e) {
  return self->setCurrentIndexFromKeyEvent(e);
}

//  bool QQuickTableViewPrivate::canEdit(const QModelIndex tappedIndex, bool
//      warn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate7canEditE11QModelIndexb(
    QQuickTableViewPrivate *self,
    const QModelIndex *tappedIndex,
    bool warn) {
  return self->canEdit(*tappedIndex, warn);
}

//  bool QQuickTableViewPrivate::editFromKeyEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate16editFromKeyEventEP9QKeyEvent(
    QQuickTableViewPrivate *self,
    QKeyEvent *e) {
  return self->editFromKeyEvent(e);
}

//  void QQuickTableViewPrivate::closeEditorAndCommit()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20closeEditorAndCommitEv(
    QQuickTableViewPrivate *self) {
  self->closeEditorAndCommit();
}

//  QObject
//      *QQuickTableViewPrivate::installEventFilterOnFocusObjectInsideEditIte
//      m()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQuickTableViewPrivate45installEventFilterOnFocusObjectInsideEditItemEv(
    QQuickTableViewPrivate *self) {
  return self->installEventFilterOnFocusObjectInsideEditItem();
}

//  QQuickItem *QQuickTableViewPrivate::selectionPointerHandlerTarget() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK22QQuickTableViewPrivate29selectionPointerHandlerTargetEv(
    const QQuickTableViewPrivate *self) {
  return self->selectionPointerHandlerTarget();
}

//  bool QQuickTableViewPrivate::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate12hasSelectionEv(
    const QQuickTableViewPrivate *self) {
  return self->hasSelection();
}

//  bool QQuickTableViewPrivate::startSelection(const QPointF &pos,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate14startSelectionERK7QPointF6QFlagsIN2Qt16KeyboardModifierEE(
    QQuickTableViewPrivate *self,
    const QPointF *pos,
    int modifiers) {
  return self->startSelection(
      *pos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  void QQuickTableViewPrivate::setSelectionStartPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20setSelectionStartPosERK7QPointF(
    QQuickTableViewPrivate *self,
    const QPointF *pos) {
  self->setSelectionStartPos(*pos);
}

//  void QQuickTableViewPrivate::setSelectionEndPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18setSelectionEndPosERK7QPointF(
    QQuickTableViewPrivate *self,
    const QPointF *pos) {
  self->setSelectionEndPos(*pos);
}

//  void QQuickTableViewPrivate::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate14clearSelectionEv(
    QQuickTableViewPrivate *self) {
  self->clearSelection();
}

//  void QQuickTableViewPrivate::normalizeSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate18normalizeSelectionEv(
    QQuickTableViewPrivate *self) {
  self->normalizeSelection();
}

//  QRectF QQuickTableViewPrivate::selectionRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK22QQuickTableViewPrivate18selectionRectangleEv(
    const QQuickTableViewPrivate *self) {
  return new QRectF(self->selectionRectangle());
}

//  QSizeF QQuickTableViewPrivate::scrollTowardsPoint(const QPointF &pos,
//      const QSizeF &step)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN22QQuickTableViewPrivate18scrollTowardsPointERK7QPointFRK6QSizeF(
    QQuickTableViewPrivate *self,
    const QPointF *pos,
    const QSizeF *step) {
  return new QSizeF(self->scrollTowardsPoint(*pos, *step));
}

//  void QQuickTableViewPrivate::cancelSelectionTracking()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate23cancelSelectionTrackingEv(
    QQuickTableViewPrivate *self) {
  self->cancelSelectionTracking();
}

//  QPoint QQuickTableViewPrivate::clampedCellAtPos(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK22QQuickTableViewPrivate16clampedCellAtPosERK7QPointF(
    const QQuickTableViewPrivate *self,
    const QPointF *pos) {
  return new QPoint(self->clampedCellAtPos(*pos));
}

//  void QQuickTableViewPrivate::updateSelection(const QRect &oldSelection,
//      const QRect &newSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS2_(
    QQuickTableViewPrivate *self,
    const QRect *oldSelection,
    const QRect *newSelection) {
  self->updateSelection(*oldSelection, *newSelection);
}

//  QRect QQuickTableViewPrivate::selection() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK22QQuickTableViewPrivate9selectionEv(
    const QQuickTableViewPrivate *self) {
  return new QRect(self->selection());
}

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewPrivate::initSectionDragHandler(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate22initSectionDragHandlerEN2Qt11OrientationE(
    QQuickTableViewPrivate *self,
    Qt::Orientation orientation) {
  self->initSectionDragHandler(orientation);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewPrivate::destroySectionDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate25destroySectionDragHandlerEv(
    QQuickTableViewPrivate *self) {
  self->destroySectionDragHandler();
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void QQuickTableViewPrivate::setActivePointerHandler(QQuickTableViewPoint
//      erHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate23setActivePointerHandlerEP29QQuickTableViewPointerHandler(
    QQuickTableViewPrivate *self,
    QQuickTableViewPointerHandler *handler) {
  self->setActivePointerHandler(handler);
}

//  QQuickTableViewPointerHandler
//      *QQuickTableViewPrivate::activePointerHandler() const
extern "C" Q_DECL_EXPORT
QQuickTableViewPointerHandler *ritual_ZNK22QQuickTableViewPrivate20activePointerHandlerEv(
    const QQuickTableViewPrivate *self) {
  return self->activePointerHandler();
}

//  void QQuickTableViewPrivate::moveSection(int source, int destination,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate11moveSectionEiiN2Qt11OrientationE(
    QQuickTableViewPrivate *self,
    int source,
    int destination,
    Qt::Orientation orientation) {
  self->moveSection(source, destination, orientation);
}

//  void QQuickTableViewPrivate::initializeIndexMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate22initializeIndexMappingEv(
    QQuickTableViewPrivate *self) {
  self->initializeIndexMapping();
}

//  void QQuickTableViewPrivate::clearIndexMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate17clearIndexMappingEv(
    QQuickTableViewPrivate *self) {
  self->clearIndexMapping();
}

//  void QQuickTableViewPrivate::clearSection(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate12clearSectionEN2Qt11OrientationE(
    QQuickTableViewPrivate *self,
    Qt::Orientation orientation) {
  self->clearSection(orientation);
}

//  int QQuickTableViewPrivate::logicalRowIndex(const int visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate15logicalRowIndexEi(
    const QQuickTableViewPrivate *self,
    int visualIndex) {
  return self->logicalRowIndex(visualIndex);
}

//  int QQuickTableViewPrivate::logicalColumnIndex(const int visualIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate18logicalColumnIndexEi(
    const QQuickTableViewPrivate *self,
    int visualIndex) {
  return self->logicalColumnIndex(visualIndex);
}

//  int QQuickTableViewPrivate::visualRowIndex(const int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate14visualRowIndexEi(
    const QQuickTableViewPrivate *self,
    int logicalIndex) {
  return self->visualRowIndex(logicalIndex);
}

//  int QQuickTableViewPrivate::visualColumnIndex(const int logicalIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate17visualColumnIndexEi(
    const QQuickTableViewPrivate *self,
    int logicalIndex) {
  return self->visualColumnIndex(logicalIndex);
}

//  void QQuickTableViewPrivate::setContainsDragOnDelegateItem(const
//      QModelIndex &modelIndex, bool overlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate29setContainsDragOnDelegateItemERK11QModelIndexb(
    QQuickTableViewPrivate *self,
    const QModelIndex *modelIndex,
    bool overlay) {
  self->setContainsDragOnDelegateItem(*modelIndex, overlay);
}

//  int QQuickTableViewPrivate::getEditCellIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate16getEditCellIndexERK11QModelIndex(
    const QQuickTableViewPrivate *self,
    const QModelIndex *index) {
  return self->getEditCellIndex(*index);
}

//  QQuickTableViewPrivate as the QQuickSelectable it is built on
extern "C" Q_DECL_EXPORT
QQuickSelectable *ritual_cast_QQuickTableViewPrivate_QQuickSelectable(
    QQuickTableViewPrivate *self) {
  return static_cast<QQuickSelectable *>(self);
}

//  a Python function taken by a CuteQQuickTableViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTableViewPrivate(
    QQuickTableViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTableViewPrivate *>(self)->take(key, call);
}

//  void QQuickTableViewPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate12updatePolishEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::updatePolish();
}

//  void QQuickTableViewPrivate::initItemCallback(int modelIndex, QObject
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *item) {
  self->QQuickTableViewPrivate::initItemCallback(modelIndex, item);
}

//  void QQuickTableViewPrivate::itemCreatedCallback(int modelIndex, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *object) {
  self->QQuickTableViewPrivate::itemCreatedCallback(modelIndex, object);
}

//  void QQuickTableViewPrivate::itemPooledCallback(int modelIndex, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *object) {
  self->QQuickTableViewPrivate::itemPooledCallback(modelIndex, object);
}

//  void QQuickTableViewPrivate::itemReusedCallback(int modelIndex, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject(
    QQuickTableViewPrivate *self,
    int modelIndex,
    QObject *object) {
  self->QQuickTableViewPrivate::itemReusedCallback(modelIndex, object);
}

//  void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet &changeSet,
//      bool reset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb(
    QQuickTableViewPrivate *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->QQuickTableViewPrivate::modelUpdated(*changeSet, reset);
}

//  void QQuickTableViewPrivate::updateItemProperties(int flatIndex, QObject
//      *object, bool init)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObjectb(
    QQuickTableViewPrivate *self,
    int flatIndex,
    QObject *object,
    bool init) {
  self->QQuickTableViewPrivate::updateItemProperties(
      flatIndex,
      object,
      init);
}

//  void QQuickTableViewPrivate::syncWithPendingChanges()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::syncWithPendingChanges();
}

//  void QQuickTableViewPrivate::syncDelegate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate12syncDelegateEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::syncDelegate();
}

//  void QQuickTableViewPrivate::syncDelegateModelAccess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::syncDelegateModelAccess();
}

//  QVariant QQuickTableViewPrivate::modelImpl() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QQuickTableViewPrivate9modelImplEv(
    const QQuickTableViewPrivate *self) {
  return new QVariant(self->QQuickTableViewPrivate::modelImpl());
}

//  void QQuickTableViewPrivate::setModelImpl(const QVariant &newModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant(
    QQuickTableViewPrivate *self,
    const QVariant *newModel) {
  self->QQuickTableViewPrivate::setModelImpl(*newModel);
}

//  void QQuickTableViewPrivate::syncModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate9syncModelEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::syncModel();
}

//  void QQuickTableViewPrivate::syncSyncView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate12syncSyncViewEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::syncSyncView();
}

//  void QQuickTableViewPrivate::syncPositionView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate16syncPositionViewEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::syncPositionView();
}

//  QAbstractItemModel *QQuickTableViewPrivate::selectionSourceModel()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_own_ZN22QQuickTableViewPrivate20selectionSourceModelEv(
    QQuickTableViewPrivate *self) {
  return self->QQuickTableViewPrivate::selectionSourceModel();
}

//  QQuickItem *QQuickTableViewPrivate::selectionPointerHandlerTarget() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZNK22QQuickTableViewPrivate29selectionPointerHandlerTargetEv(
    const QQuickTableViewPrivate *self) {
  return self->QQuickTableViewPrivate::selectionPointerHandlerTarget();
}

//  bool QQuickTableViewPrivate::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QQuickTableViewPrivate12hasSelectionEv(
    const QQuickTableViewPrivate *self) {
  return self->QQuickTableViewPrivate::hasSelection();
}

//  bool QQuickTableViewPrivate::startSelection(const QPointF &pos,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickTableViewPrivate14startSelectionERK7QPointF6QFlagsIN2Qt16KeyboardModifierEE(
    QQuickTableViewPrivate *self,
    const QPointF *pos,
    int modifiers) {
  return self->QQuickTableViewPrivate::startSelection(
      *pos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  void QQuickTableViewPrivate::setSelectionStartPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate20setSelectionStartPosERK7QPointF(
    QQuickTableViewPrivate *self,
    const QPointF *pos) {
  self->QQuickTableViewPrivate::setSelectionStartPos(*pos);
}

//  void QQuickTableViewPrivate::setSelectionEndPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate18setSelectionEndPosERK7QPointF(
    QQuickTableViewPrivate *self,
    const QPointF *pos) {
  self->QQuickTableViewPrivate::setSelectionEndPos(*pos);
}

//  void QQuickTableViewPrivate::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate14clearSelectionEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::clearSelection();
}

//  void QQuickTableViewPrivate::normalizeSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate18normalizeSelectionEv(
    QQuickTableViewPrivate *self) {
  self->QQuickTableViewPrivate::normalizeSelection();
}

//  QRectF QQuickTableViewPrivate::selectionRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK22QQuickTableViewPrivate18selectionRectangleEv(
    const QQuickTableViewPrivate *self) {
  return new QRectF(self->QQuickTableViewPrivate::selectionRectangle());
}

//  QSizeF QQuickTableViewPrivate::scrollTowardsPoint(const QPointF &pos,
//      const QSizeF &step)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZN22QQuickTableViewPrivate18scrollTowardsPointERK7QPointFRK6QSizeF(
    QQuickTableViewPrivate *self,
    const QPointF *pos,
    const QSizeF *step) {
  return new QSizeF(
      self->QQuickTableViewPrivate::scrollTowardsPoint(
          *pos,
          *step));
}

//  void QQuickTableViewPrivate::updateSelection(const QRect &oldSelection,
//      const QRect &newSelection)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS2_(
    QQuickTableViewPrivate *self,
    const QRect *oldSelection,
    const QRect *newSelection) {
  self->QQuickTableViewPrivate::updateSelection(
      *oldSelection,
      *newSelection);
}

//  int QQuickTableViewPrivate::logicalRowIndex(const int visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQuickTableViewPrivate15logicalRowIndexEi(
    const QQuickTableViewPrivate *self,
    int visualIndex) {
  return self->QQuickTableViewPrivate::logicalRowIndex(visualIndex);
}

//  int QQuickTableViewPrivate::logicalColumnIndex(const int visualIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQuickTableViewPrivate18logicalColumnIndexEi(
    const QQuickTableViewPrivate *self,
    int visualIndex) {
  return self->QQuickTableViewPrivate::logicalColumnIndex(visualIndex);
}

//  int QQuickTableViewPrivate::visualRowIndex(const int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQuickTableViewPrivate14visualRowIndexEi(
    const QQuickTableViewPrivate *self,
    int logicalIndex) {
  return self->QQuickTableViewPrivate::visualRowIndex(logicalIndex);
}

//  int QQuickTableViewPrivate::visualColumnIndex(const int logicalIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQuickTableViewPrivate17visualColumnIndexEi(
    const QQuickTableViewPrivate *self,
    int logicalIndex) {
  return self->QQuickTableViewPrivate::visualColumnIndex(logicalIndex);
}
