//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktreeview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_treeview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktreeview_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktreeview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickTreeViewPrivate that Python can take functions over in. Every QQuickTreeViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQuickTreeViewPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall1)(const void *, const QVariant *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall2)(const void *, int, QObject *, bool, int *);
typedef void (*CuteQQuickTreeViewPrivateCall3)(const void *, const QRect *, const QRect *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall5)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall6)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall7)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall8)(const void *, int, QObject *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall9)(const void *, const QQmlChangeSet *, bool, int *);
typedef void (*CuteQQuickTreeViewPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall15)(const void *, int *);
typedef void * (*CuteQQuickTreeViewPrivateCall16)(const void *, int *);
typedef void * (*CuteQQuickTreeViewPrivateCall17)(const void *, int *);
typedef bool (*CuteQQuickTreeViewPrivateCall18)(const void *, int *);
typedef bool (*CuteQQuickTreeViewPrivateCall19)(const void *, const QPointF *, int, int *);
typedef void (*CuteQQuickTreeViewPrivateCall20)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall21)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall23)(const void *, int *);
typedef const QRectF * (*CuteQQuickTreeViewPrivateCall24)(const void *, int *);
typedef const QSizeF * (*CuteQQuickTreeViewPrivateCall25)(const void *, const QPointF *, const QSizeF *, int *);
typedef int (*CuteQQuickTreeViewPrivateCall26)(const void *, int, int *);
typedef int (*CuteQQuickTreeViewPrivateCall27)(const void *, int, int *);
typedef int (*CuteQQuickTreeViewPrivateCall28)(const void *, int, int *);
typedef int (*CuteQQuickTreeViewPrivateCall29)(const void *, int, int *);
typedef void (*CuteQQuickTreeViewPrivateCall30)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall31)(const void *, QQuickPointerHandler *, int *);
typedef bool (*CuteQQuickTreeViewPrivateCall32)(const void *, const QPointerEvent *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall33)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTreeViewPrivateCall34)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall35)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTreeViewPrivateCall36)(const void *, int, int *);
typedef qreal (*CuteQQuickTreeViewPrivateCall37)(const void *, int *);
typedef qreal (*CuteQQuickTreeViewPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall39)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall40)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTreeViewPrivateCall41)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickTreeViewPrivateCall42)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickTreeViewPrivateCall43)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTreeViewPrivateCall44)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickTreeViewPrivateCall45)(const void *, bool, int *);
typedef void * (*CuteQQuickTreeViewPrivateCall46)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall47)(const void *, int *);
typedef void (*CuteQQuickTreeViewPrivateCall48)(const void *, int, int *);
class CuteQQuickTreeViewPrivate : public QQuickTreeViewPrivate {
public:
  using QQuickTreeViewPrivate::QQuickTreeViewPrivate;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QQuickTableViewPrivate9modelImplEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObjectb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12syncDelegateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate9syncModelEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate12syncSyncViewEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate16syncPositionViewEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTableViewPrivate20selectionSourceModelEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable29selectionPointerHandlerTargetEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable12hasSelectionEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable14startSelectionERK7QPointF6QFlagsIN2Qt16KeyboardModifierEE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable20setSelectionStartPosERK7QPointF")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18setSelectionEndPosERK7QPointF")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable14clearSelectionEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18normalizeSelectionEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable18selectionRectangleEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18scrollTowardsPointERK7QPointFRK6QSizeF")) {
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

  //  QVariant QQuickTreeViewPrivate::modelImpl() const
  QVariant modelImpl() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall0 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall0>(taken[0]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTreeViewPrivate::modelImpl();
  }

  //  void QQuickTreeViewPrivate::setModelImpl(const QVariant &newModel)
  void setModelImpl(const QVariant &newModel) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall1 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall1>(taken[1]);
      call(this, &newModel, &handled);
      if (handled) return;
    }
    QQuickTreeViewPrivate::setModelImpl(newModel);
  }

  //  void QQuickTreeViewPrivate::updateItemProperties(int flatIndex,
  //      QObject *object, bool init)
  void updateItemProperties(
      int flatIndex,
      QObject *object,
      bool init) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall2 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall2>(taken[2]);
      call(this, flatIndex, object, init, &handled);
      if (handled) return;
    }
    QQuickTreeViewPrivate::updateItemProperties(flatIndex, object, init);
  }

  //  void QQuickTreeViewPrivate::updateSelection(const QRect
  //      &oldSelection, const QRect &newSelection)
  void updateSelection(
      const QRect &oldSelection,
      const QRect &newSelection) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall3 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall3>(taken[3]);
      call(this, &oldSelection, &newSelection, &handled);
      if (handled) return;
    }
    QQuickTreeViewPrivate::updateSelection(oldSelection, newSelection);
  }

  //  void QQuickTableViewPrivate::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall4 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::updatePolish();
  }

  //  void QQuickTableViewPrivate::initItemCallback(int modelIndex, QObject
  //      *item)
  void initItemCallback(int modelIndex, QObject *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall5 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall5>(taken[5]);
      call(this, modelIndex, item, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::initItemCallback(modelIndex, item);
  }

  //  void QQuickTableViewPrivate::itemCreatedCallback(int modelIndex,
  //      QObject *object)
  void itemCreatedCallback(int modelIndex, QObject *object) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall6 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall6>(taken[6]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemCreatedCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::itemPooledCallback(int modelIndex,
  //      QObject *object)
  void itemPooledCallback(int modelIndex, QObject *object) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall7 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall7>(taken[7]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemPooledCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::itemReusedCallback(int modelIndex,
  //      QObject *object)
  void itemReusedCallback(int modelIndex, QObject *object) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall8 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall8>(taken[8]);
      call(this, modelIndex, object, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::itemReusedCallback(modelIndex, object);
  }

  //  void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet
  //      &changeSet, bool reset)
  void modelUpdated(const QQmlChangeSet &changeSet, bool reset) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall9 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall9>(taken[9]);
      call(this, &changeSet, reset, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::modelUpdated(changeSet, reset);
  }

  //  void QQuickTableViewPrivate::syncWithPendingChanges()
  void syncWithPendingChanges() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall10 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncWithPendingChanges();
  }

  //  void QQuickTableViewPrivate::syncDelegate()
  void syncDelegate() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall11 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncDelegate();
  }

  //  void QQuickTableViewPrivate::syncDelegateModelAccess()
  void syncDelegateModelAccess() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall12 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncDelegateModelAccess();
  }

  //  void QQuickTableViewPrivate::syncModel()
  void syncModel() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall13 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncModel();
  }

  //  void QQuickTableViewPrivate::syncSyncView()
  void syncSyncView() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall14 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncSyncView();
  }

  //  void QQuickTableViewPrivate::syncPositionView()
  void syncPositionView() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall15 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::syncPositionView();
  }

  //  QAbstractItemModel *QQuickTableViewPrivate::selectionSourceModel()
  QAbstractItemModel *selectionSourceModel() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall16 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractItemModel *>(given);
    }
    return QQuickTableViewPrivate::selectionSourceModel();
  }

  //  QQuickItem *QQuickTableViewPrivate::selectionPointerHandlerTarget()
  //      const
  QQuickItem *selectionPointerHandlerTarget() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall17 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickTableViewPrivate::selectionPointerHandlerTarget();
  }

  //  bool QQuickTableViewPrivate::hasSelection() const
  bool hasSelection() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall18 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall19 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall19>(taken[19]);
      bool given = call(this, &pos, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return QQuickTableViewPrivate::startSelection(pos, modifiers);
  }

  //  void QQuickTableViewPrivate::setSelectionStartPos(const QPointF &pos)
  void setSelectionStartPos(const QPointF &pos) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall20 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall20>(taken[20]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setSelectionStartPos(pos);
  }

  //  void QQuickTableViewPrivate::setSelectionEndPos(const QPointF &pos)
  void setSelectionEndPos(const QPointF &pos) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall21 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall21>(taken[21]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::setSelectionEndPos(pos);
  }

  //  void QQuickTableViewPrivate::clearSelection()
  void clearSelection() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall22 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::clearSelection();
  }

  //  void QQuickTableViewPrivate::normalizeSelection()
  void normalizeSelection() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall23 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableViewPrivate::normalizeSelection();
  }

  //  QRectF QQuickTableViewPrivate::selectionRectangle() const
  QRectF selectionRectangle() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall24 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall25 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall25>(taken[25]);
      const QSizeF * given = call(this, &pos, &step, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableViewPrivate::scrollTowardsPoint(pos, step);
  }

  //  int QQuickTableViewPrivate::logicalRowIndex(const int visualIndex)
  //      const
  int logicalRowIndex(const int visualIndex) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall26 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall26>(taken[26]);
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
      CuteQQuickTreeViewPrivateCall27 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall27>(taken[27]);
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
      CuteQQuickTreeViewPrivateCall28 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall28>(taken[28]);
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
      CuteQQuickTreeViewPrivateCall29 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall29>(taken[29]);
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
      CuteQQuickTreeViewPrivateCall30 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall30>(taken[30]);
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
      CuteQQuickTreeViewPrivateCall31 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall31>(taken[31]);
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
      CuteQQuickTreeViewPrivateCall32 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall32>(taken[32]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickFlickablePrivate::wantsPointerEvent(a0);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall33 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall33>(taken[33]);
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
      CuteQQuickTreeViewPrivateCall34 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall34>(taken[34]);
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
      CuteQQuickTreeViewPrivateCall35 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall35>(taken[35]);
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
      CuteQQuickTreeViewPrivateCall36 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall36>(taken[36]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall37 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall37>(taken[37]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall38 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall38>(taken[38]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall39 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall40 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall40>(taken[40]);
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
      CuteQQuickTreeViewPrivateCall41 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall41>(taken[41]);
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
      CuteQQuickTreeViewPrivateCall42 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall42>(taken[42]);
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
      CuteQQuickTreeViewPrivateCall43 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall43>(taken[43]);
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
      CuteQQuickTreeViewPrivateCall44 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall44>(taken[44]);
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
      CuteQQuickTreeViewPrivateCall45 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall45>(taken[45]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall46 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall46>(taken[46]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall47 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickTreeViewPrivateCall48 call = reinterpret_cast<CuteQQuickTreeViewPrivateCall48>(taken[48]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickTreeView *QQuickTreeViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTreeView *ritual_ZN21QQuickTreeViewPrivate6q_funcEv(
    QQuickTreeViewPrivate *self) {
  return self->q_func();
}

//  const QQuickTreeView *QQuickTreeViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTreeView *ritual_ZNK21QQuickTreeViewPrivate6q_funcEv(
    const QQuickTreeViewPrivate *self) {
  return self->q_func();
}

//  QQuickTreeViewPrivate::QQuickTreeViewPrivate()
extern "C" Q_DECL_EXPORT
QQuickTreeViewPrivate *ritual_ZN21QQuickTreeViewPrivateC1Ev() {
  return new CuteQQuickTreeViewPrivate();
}

//  QQuickTreeViewPrivate::~QQuickTreeViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTreeViewPrivateD1Ev(QQuickTreeViewPrivate *self) {
  delete self;
}

//  QQuickTreeViewPrivate *QQuickTreeViewPrivate::get(QQuickTreeView *q)
extern "C" Q_DECL_EXPORT
QQuickTreeViewPrivate *ritual_ZN21QQuickTreeViewPrivate3getEP14QQuickTreeView(
    QQuickTreeView *q) {
  return QQuickTreeViewPrivate::get(q);
}

//  QVariant QQuickTreeViewPrivate::modelImpl() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickTreeViewPrivate9modelImplEv(
    const QQuickTreeViewPrivate *self) {
  return new QVariant(self->modelImpl());
}

//  void QQuickTreeViewPrivate::setModelImpl(const QVariant &newModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTreeViewPrivate12setModelImplERK8QVariant(
    QQuickTreeViewPrivate *self,
    const QVariant *newModel) {
  self->setModelImpl(*newModel);
}

//  void QQuickTreeViewPrivate::updateItemProperties(int flatIndex, QObject
//      *object, bool init)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTreeViewPrivate20updateItemPropertiesEiP7QObjectb(
    QQuickTreeViewPrivate *self,
    int flatIndex,
    QObject *object,
    bool init) {
  self->updateItemProperties(flatIndex, object, init);
}

//  void QQuickTreeViewPrivate::updateSelection(const QRect &oldSelection,
//      const QRect &newSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTreeViewPrivate15updateSelectionERK5QRectS2_(
    QQuickTreeViewPrivate *self,
    const QRect *oldSelection,
    const QRect *newSelection) {
  self->updateSelection(*oldSelection, *newSelection);
}

//  a Python function taken by a CuteQQuickTreeViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTreeViewPrivate(
    QQuickTreeViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTreeViewPrivate *>(self)->take(key, call);
}

//  QVariant QQuickTreeViewPrivate::modelImpl() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QQuickTreeViewPrivate9modelImplEv(
    const QQuickTreeViewPrivate *self) {
  return new QVariant(self->QQuickTreeViewPrivate::modelImpl());
}

//  void QQuickTreeViewPrivate::setModelImpl(const QVariant &newModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTreeViewPrivate12setModelImplERK8QVariant(
    QQuickTreeViewPrivate *self,
    const QVariant *newModel) {
  self->QQuickTreeViewPrivate::setModelImpl(*newModel);
}

//  void QQuickTreeViewPrivate::updateItemProperties(int flatIndex, QObject
//      *object, bool init)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTreeViewPrivate20updateItemPropertiesEiP7QObjectb(
    QQuickTreeViewPrivate *self,
    int flatIndex,
    QObject *object,
    bool init) {
  self->QQuickTreeViewPrivate::updateItemProperties(flatIndex, object, init);
}

//  void QQuickTreeViewPrivate::updateSelection(const QRect &oldSelection,
//      const QRect &newSelection)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTreeViewPrivate15updateSelectionERK5QRectS2_(
    QQuickTreeViewPrivate *self,
    const QRect *oldSelection,
    const QRect *newSelection) {
  self->QQuickTreeViewPrivate::updateSelection(*oldSelection, *newSelection);
}

#endif  // QT_CONFIG(quick_treeview)
