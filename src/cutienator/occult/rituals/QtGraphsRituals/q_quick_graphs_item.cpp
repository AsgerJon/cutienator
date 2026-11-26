//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsitem_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: the ritual of calculateLabelRotation(float) is
//  taken out, as Qt declares it but its library does not define it.
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGraphs/qabstract3dseries.h>
#include <QtGraphs/qabstract3daxis.h>
#include <QtGraphs/qgraphstheme.h>
#include <QtGui/qimage.h>
#include <QtGraphs/qcustom3ditem.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickGraphsItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsItem : QQuickGraphsItem {
  using QQuickGraphsItem::event;
  using QQuickGraphsItem::handleWindowChanged;
  using QQuickGraphsItem::itemChange;
  using QQuickGraphsItem::updateWindowParameters;
  using QQuickGraphsItem::handleSelectionModeChange;
  using QQuickGraphsItem::handleShadowQualityChange;
  using QQuickGraphsItem::handleSelectedElementChange;
  using QQuickGraphsItem::handleOptimizationHintChange;
  using QQuickGraphsItem::keyPressEvent;
  using QQuickGraphsItem::handleThemeTypeChange;
  using QQuickGraphsItem::handleParentWidthChange;
  using QQuickGraphsItem::handleParentHeightChange;
  using QQuickGraphsItem::componentComplete;
  using QQuickGraphsItem::createSliceView;
  using QQuickGraphsItem::calculateCategoryLabelPosition;
  using QQuickGraphsItem::calculateCategoryGridLinePosition;
  using QQuickGraphsItem::updateShadowQuality;
  using QQuickGraphsItem::updateSliceItemLabel;
  using QQuickGraphsItem::synchData;
  using QQuickGraphsItem::updateGraph;
  using QQuickGraphsItem::toggleSliceGraph;
  using QQuickGraphsItem::updateAxisRange;
  using QQuickGraphsItem::updateAxisReversed;
  using QQuickGraphsItem::updateSingleHighlightColor;
  using QQuickGraphsItem::updateLightStrength;
  using QQuickGraphsItem::handleLabelCountChanged;
  using QQuickGraphsItem::createDefaultAxis;
  using QQuickGraphsItem::startRecordingRemovesAndInserts;
};

//  A QQuickGraphsItem that Python can take functions over in. Every QQuickGraphsItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsItemCall0)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall1)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall2)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall3)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall4)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall5)(const void *, int, bool, int *);
typedef void (*CuteQQuickGraphsItemCall6)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall7)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall8)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall9)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall10)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall11)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall12)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall13)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall14)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall15)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall16)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsItemCall17)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall18)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall19)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsItemCall20)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsItemCall21)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsItemCall22)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsItemCall23)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsItemCall24)(const void *, int, int *);
typedef int (*CuteQQuickGraphsItemCall25)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall26)(const void *, int, int *);
typedef int (*CuteQQuickGraphsItemCall27)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall28)(const void *, int, int *);
typedef int (*CuteQQuickGraphsItemCall29)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall30)(const void *, int, int *);
typedef int (*CuteQQuickGraphsItemCall31)(const void *, int *);
typedef int (*CuteQQuickGraphsItemCall32)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall33)(const void *, int, int *);
typedef int (*CuteQQuickGraphsItemCall34)(const void *, int *);
typedef bool (*CuteQQuickGraphsItemCall35)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsItemCall36)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsItemCall37)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsItemCall38)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall39)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsItemCall40)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsItemCall41)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsItemCall42)(const void *, int *);
typedef void * (*CuteQQuickGraphsItemCall43)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsItemCall44)(const void *, int *);
typedef void * (*CuteQQuickGraphsItemCall45)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall46)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickGraphsItemCall47)(const void *, int, int *);
typedef bool (*CuteQQuickGraphsItemCall48)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsItemCall49)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsItemCall50)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsItemCall51)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsItemCall52)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsItemCall53)(const void *, bool, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsItemCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsItemCall55)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall56)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsItemCall57)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall58)(const void *, int, int *);
typedef void (*CuteQQuickGraphsItemCall59)(const void *, int, int *);
typedef void (*CuteQQuickGraphsItemCall60)(const void *, int, int *);
typedef void (*CuteQQuickGraphsItemCall61)(const void *, int, int *);
typedef void (*CuteQQuickGraphsItemCall62)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall63)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall64)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall65)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall66)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall67)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall68)(const void *, int *);
typedef const QVector3D * (*CuteQQuickGraphsItemCall69)(const void *, QAbstract3DAxis *, const QVector3D *, int, int *);
typedef float (*CuteQQuickGraphsItemCall70)(const void *, QAbstract3DAxis *, int, int *);
typedef void (*CuteQQuickGraphsItemCall71)(const void *, int, int *);
typedef void (*CuteQQuickGraphsItemCall72)(const void *, const QString *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsItemCall73)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall74)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall75)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall76)(const void *, float, float, int *);
typedef void (*CuteQQuickGraphsItemCall77)(const void *, bool, int *);
typedef void (*CuteQQuickGraphsItemCall78)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall79)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall80)(const void *, QQuick3DRepeater *, const QColor *, int *);
typedef void * (*CuteQQuickGraphsItemCall81)(const void *, QAbstract3DSeries *, int, int *);
typedef void * (*CuteQQuickGraphsItemCall82)(const void *, int, int *);
typedef void (*CuteQQuickGraphsItemCall83)(const void *, int *);
typedef bool (*CuteQQuickGraphsItemCall84)(const void *, int *);
typedef void * (*CuteQQuickGraphsItemCall85)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall86)(const void *, int *);
typedef void * (*CuteQQuickGraphsItemCall87)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQQuickGraphsItemCall88)(const void *, int *);
typedef const QRectF * (*CuteQQuickGraphsItemCall89)(const void *, int *);
typedef bool (*CuteQQuickGraphsItemCall90)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickGraphsItemCall91)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsItemCall92)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall93)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickGraphsItemCall94)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsItemCall95)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall96)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall97)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall98)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall99)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall100)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall101)(const void *, int *);
typedef void (*CuteQQuickGraphsItemCall102)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsItemCall103)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsItemCall104)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall105)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall106)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall107)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsItemCall108)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsItemCall109)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsItemCall110)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsItemCall111)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickGraphsItemCall112)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickGraphsItemCall113)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsItemCall114)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsItemCall115)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsItemCall116)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsItemCall117)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsItemCall118)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsItemCall119)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsItem : public QQuickGraphsItem {
public:
  using QQuickGraphsItem::QQuickGraphsItem;
  void *taken[120] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7QObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySenderEP7QObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7QObject")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySenderEP7QObject")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySenderEP7QObject")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QObject")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySenderEP7QObject")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySenderEP7QObject")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QObject")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7QObject")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7QObject")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleLightingModeChangedEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16adjustAxisRangesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxis")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSeries")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13RenderingModeE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13renderingModeEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem21transparencyTechniqueEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13selectionModeEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13shadowQualityEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem15selectedElementEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14setMsaaSamplesEi")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem11msaaSamplesEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14clearSelectionEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17removeCustomItemsEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedLabelIndexEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem12selectedAxisEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedCustomItemEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9doPickingE7QPointF")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySenderEbP7QObject")) {
      taken[53] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19handleWindowChangedEv")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22updateWindowParametersEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D13ShadowQualityE")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3D11ElementTypeE")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem21handleThemeTypeChangeEv")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleParentWidthChangeEv")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24handleParentHeightChangeEv")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15createSliceViewEv")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAbstract3DAxisi")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3D")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9synchDataEv")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11updateGraphEv")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16toggleSliceGraphEv")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15updateAxisRangeEff")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18updateAxisReversedEb")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem26updateSingleHighlightColorEv")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateLightStrengthEv")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepeater6QColor")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[90] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[91] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[93] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[94] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[102] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[103] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[107] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[108] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[109] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[110] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[111] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[113] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[114] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[115] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[116] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[117] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[118] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[119] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject
  //      *sender)
  void handleAxisTitleChangedBySender(QObject *sender) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsItemCall0 call = reinterpret_cast<CuteQQuickGraphsItemCall0>(taken[0]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject
  //      *sender)
  void handleAxisLabelsChangedBySender(QObject *sender) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsItemCall1 call = reinterpret_cast<CuteQQuickGraphsItemCall1>(taken[1]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelsChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisRangeChangedBySender(QObject
  //      *sender)
  void handleAxisRangeChangedBySender(QObject *sender) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsItemCall2 call = reinterpret_cast<CuteQQuickGraphsItemCall2>(taken[2]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisRangeChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
  //      *sender)
  void handleAxisSegmentCountChangedBySender(QObject *sender) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsItemCall3 call = reinterpret_cast<CuteQQuickGraphsItemCall3>(taken[3]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSegmentCountChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObjec
  //      t *sender)
  void handleAxisSubSegmentCountChangedBySender(QObject *sender) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsItemCall4 call = reinterpret_cast<CuteQQuickGraphsItemCall4>(taken[4]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisAutoAdjustRangeChangedInOrientation(
  //      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
  void handleAxisAutoAdjustRangeChangedInOrientation(
      QAbstract3DAxis::AxisOrientation orientation,
      bool autoAdjust) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsItemCall5 call = reinterpret_cast<CuteQQuickGraphsItemCall5>(taken[5]);
      call(this, static_cast<int>(orientation), autoAdjust, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
  //      *sender)
  void handleAxisLabelFormatChangedBySender(QObject *sender) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsItemCall6 call = reinterpret_cast<CuteQQuickGraphsItemCall6>(taken[6]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelFormatChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject
  //      *sender)
  void handleAxisReversedChangedBySender(QObject *sender) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsItemCall7 call = reinterpret_cast<CuteQQuickGraphsItemCall7>(taken[7]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisReversedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject
  //      *sender)
  void handleAxisFormatterDirtyBySender(QObject *sender) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsItemCall8 call = reinterpret_cast<CuteQQuickGraphsItemCall8>(taken[8]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisFormatterDirtyBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObj
  //      ect *sender)
  void handleAxisLabelAutoRotationChangedBySender(QObject *sender) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsItemCall9 call = reinterpret_cast<CuteQQuickGraphsItemCall9>(taken[9]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(QOb
  //      ject *sender)
  void handleAxisScaleLabelsByCountChangedBySender(
      QObject *sender) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsItemCall10 call = reinterpret_cast<CuteQQuickGraphsItemCall10>(taken[10]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
  //      *sender)
  void handleAxisLabelSizeChangedBySender(QObject *sender) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsItemCall11 call = reinterpret_cast<CuteQQuickGraphsItemCall11>(taken[11]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelSizeChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisTitleVisibilityChangedBySender(QObject *sender) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsItemCall12 call = reinterpret_cast<CuteQQuickGraphsItemCall12>(taken[12]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisLabelVisibilityChangedBySender(QObject *sender) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsItemCall13 call = reinterpret_cast<CuteQQuickGraphsItemCall13>(taken[13]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
  //      *sender)
  void handleAxisTitleFixedChangedBySender(QObject *sender) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsItemCall14 call = reinterpret_cast<CuteQQuickGraphsItemCall14>(taken[14]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleFixedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
  //      *sender)
  void handleAxisTitleOffsetChangedBySender(QObject *sender) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsItemCall15 call = reinterpret_cast<CuteQQuickGraphsItemCall15>(taken[15]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleSeriesVisibilityChangedBySender(QObject
  //      *sender)
  void handleSeriesVisibilityChangedBySender(QObject *sender) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsItemCall16 call = reinterpret_cast<CuteQQuickGraphsItemCall16>(taken[16]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSeriesVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleLightingModeChanged()
  void handleLightingModeChanged() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsItemCall17 call = reinterpret_cast<CuteQQuickGraphsItemCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsItem::adjustAxisRanges()
  void adjustAxisRanges() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGraphsItemCall18 call = reinterpret_cast<CuteQQuickGraphsItemCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsItem::handleMultiAxisChanged(QAbstract3DAxis *axis)
  void handleMultiAxisChanged(QAbstract3DAxis *axis) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickGraphsItemCall19 call = reinterpret_cast<CuteQQuickGraphsItemCall19>(taken[19]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleMultiAxisChanged(axis);
  }

  //  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickGraphsItemCall20 call = reinterpret_cast<CuteQQuickGraphsItemCall20>(taken[20]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addSeriesInternal(series);
  }

  //  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries
  //      *series)
  void removeSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickGraphsItemCall21 call = reinterpret_cast<CuteQQuickGraphsItemCall21>(taken[21]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeSeriesInternal(series);
  }

  //  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
  void addAxis(QAbstract3DAxis *axis) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsItemCall22 call = reinterpret_cast<CuteQQuickGraphsItemCall22>(taken[22]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addAxis(axis);
  }

  //  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
  void releaseAxis(QAbstract3DAxis *axis) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsItemCall23 call = reinterpret_cast<CuteQQuickGraphsItemCall23>(taken[23]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseAxis(axis);
  }

  //  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode
  //      mode)
  void setRenderingMode(QtGraphs3D::RenderingMode mode) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGraphsItemCall24 call = reinterpret_cast<CuteQQuickGraphsItemCall24>(taken[24]);
      call(this, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setRenderingMode(mode);
  }

  //  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
  QtGraphs3D::RenderingMode renderingMode() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickGraphsItemCall25 call = reinterpret_cast<CuteQQuickGraphsItemCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::RenderingMode>(given);
    }
    return QQuickGraphsItem::renderingMode();
  }

  //  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::Transpare
  //      ncyTechnique technique)
  void setTransparencyTechnique(
      QtGraphs3D::TransparencyTechnique technique) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickGraphsItemCall26 call = reinterpret_cast<CuteQQuickGraphsItemCall26>(taken[26]);
      call(this, static_cast<int>(technique), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setTransparencyTechnique(technique);
  }

  //  QtGraphs3D::TransparencyTechnique
  //      QQuickGraphsItem::transparencyTechnique() const
  QtGraphs3D::TransparencyTechnique transparencyTechnique() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickGraphsItemCall27 call = reinterpret_cast<CuteQQuickGraphsItemCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::TransparencyTechnique>(given);
    }
    return QQuickGraphsItem::transparencyTechnique();
  }

  //  void QQuickGraphsItem::setSelectionMode(QtGraphs3D::SelectionFlags
  //      mode)
  void setSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGraphsItemCall28 call = reinterpret_cast<CuteQQuickGraphsItemCall28>(taken[28]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setSelectionMode(mode);
  }

  //  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
  QtGraphs3D::SelectionFlags selectionMode() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickGraphsItemCall29 call = reinterpret_cast<CuteQQuickGraphsItemCall29>(taken[29]);
      int given = call(this, &handled);
      if (handled) return QFlags<QtGraphs3D::SelectionFlag>::fromInt(given);
    }
    return QQuickGraphsItem::selectionMode();
  }

  //  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void setShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickGraphsItemCall30 call = reinterpret_cast<CuteQQuickGraphsItemCall30>(taken[30]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setShadowQuality(quality);
  }

  //  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
  QtGraphs3D::ShadowQuality shadowQuality() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickGraphsItemCall31 call = reinterpret_cast<CuteQQuickGraphsItemCall31>(taken[31]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ShadowQuality>(given);
    }
    return QQuickGraphsItem::shadowQuality();
  }

  //  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
  QtGraphs3D::ElementType selectedElement() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickGraphsItemCall32 call = reinterpret_cast<CuteQQuickGraphsItemCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ElementType>(given);
    }
    return QQuickGraphsItem::selectedElement();
  }

  //  void QQuickGraphsItem::setMsaaSamples(int samples)
  void setMsaaSamples(int samples) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickGraphsItemCall33 call = reinterpret_cast<CuteQQuickGraphsItemCall33>(taken[33]);
      call(this, samples, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setMsaaSamples(samples);
  }

  //  int QQuickGraphsItem::msaaSamples() const
  int msaaSamples() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickGraphsItemCall34 call = reinterpret_cast<CuteQQuickGraphsItemCall34>(taken[34]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::msaaSamples();
  }

  //  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickGraphsItemCall35 call = reinterpret_cast<CuteQQuickGraphsItemCall35>(taken[35]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::hasSeries(series);
  }

  //  void QQuickGraphsItem::clearSelection()
  void clearSelection() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickGraphsItemCall36 call = reinterpret_cast<CuteQQuickGraphsItemCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickGraphsItemCall37 call = reinterpret_cast<CuteQQuickGraphsItemCall37>(taken[37]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::addCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItems()
  void removeCustomItems() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickGraphsItemCall38 call = reinterpret_cast<CuteQQuickGraphsItemCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItems();
  }

  //  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickGraphsItemCall39 call = reinterpret_cast<CuteQQuickGraphsItemCall39>(taken[39]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickGraphsItemCall40 call = reinterpret_cast<CuteQQuickGraphsItemCall40>(taken[40]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItemAt(position);
  }

  //  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickGraphsItemCall41 call = reinterpret_cast<CuteQQuickGraphsItemCall41>(taken[41]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseCustomItem(item);
  }

  //  int QQuickGraphsItem::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickGraphsItemCall42 call = reinterpret_cast<CuteQQuickGraphsItemCall42>(taken[42]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickGraphsItemCall43 call = reinterpret_cast<CuteQQuickGraphsItemCall43>(taken[43]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::selectedAxis();
  }

  //  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickGraphsItemCall44 call = reinterpret_cast<CuteQQuickGraphsItemCall44>(taken[44]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickGraphsItemCall45 call = reinterpret_cast<CuteQQuickGraphsItemCall45>(taken[45]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCustom3DItem *>(given);
    }
    return QQuickGraphsItem::selectedCustomItem();
  }

  //  void QQuickGraphsItem::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickGraphsItemCall46 call = reinterpret_cast<CuteQQuickGraphsItemCall46>(taken[46]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickGraphsItem::updateSelectionMode(QtGraphs3D::SelectionFlags
  //      newMode)
  void updateSelectionMode(QtGraphs3D::SelectionFlags newMode) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickGraphsItemCall47 call = reinterpret_cast<CuteQQuickGraphsItemCall47>(taken[47]);
      call(this, static_cast<int>(newMode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSelectionMode(newMode);
  }

  //  bool QQuickGraphsItem::doPicking(QPointF point)
  bool doPicking(QPointF point) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickGraphsItemCall48 call = reinterpret_cast<CuteQQuickGraphsItemCall48>(taken[48]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::doPicking(point);
  }

  //  bool QQuickGraphsItem::doRayPicking(QVector3D origin, QVector3D
  //      direction)
  bool doRayPicking(QVector3D origin, QVector3D direction) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickGraphsItemCall49 call = reinterpret_cast<CuteQQuickGraphsItemCall49>(taken[49]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::doRayPicking(origin, direction);
  }

  //  void QQuickGraphsItem::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickGraphsItemCall50 call = reinterpret_cast<CuteQQuickGraphsItemCall50>(taken[50]);
      call(this, axis, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsItem::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickGraphsItemCall51 call = reinterpret_cast<CuteQQuickGraphsItemCall51>(taken[51]);
      call(this, axis, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsItem::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickGraphsItemCall52 call = reinterpret_cast<CuteQQuickGraphsItemCall52>(taken[52]);
      call(this, axis, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsItem::handleItemLabelVisibleChangedBySender(bool
  //      visible, QObject *sender)
  void handleItemLabelVisibleChangedBySender(
      bool visible,
      QObject *sender) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickGraphsItemCall53 call = reinterpret_cast<CuteQQuickGraphsItemCall53>(taken[53]);
      call(this, visible, sender, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickGraphsItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickGraphsItemCall54 call = reinterpret_cast<CuteQQuickGraphsItemCall54>(taken[54]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickGraphsItem::handleWindowChanged()
  void handleWindowChanged() override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickGraphsItemCall55 call = reinterpret_cast<CuteQQuickGraphsItemCall55>(taken[55]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleWindowChanged();
  }

  //  void QQuickGraphsItem::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickGraphsItemCall56 call = reinterpret_cast<CuteQQuickGraphsItemCall56>(taken[56]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::itemChange(change, value);
  }

  //  void QQuickGraphsItem::updateWindowParameters()
  void updateWindowParameters() override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickGraphsItemCall57 call = reinterpret_cast<CuteQQuickGraphsItemCall57>(taken[57]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateWindowParameters();
  }

  //  void QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::Selectio
  //      nFlags mode)
  void handleSelectionModeChange(QtGraphs3D::SelectionFlags mode) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickGraphsItemCall58 call = reinterpret_cast<CuteQQuickGraphsItemCall58>(taken[58]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSelectionModeChange(mode);
  }

  //  void
  //      QQuickGraphsItem::handleShadowQualityChange(QtGraphs3D::ShadowQua
  //      lity quality)
  void handleShadowQualityChange(
      QtGraphs3D::ShadowQuality quality) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickGraphsItemCall59 call = reinterpret_cast<CuteQQuickGraphsItemCall59>(taken[59]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleShadowQualityChange(quality);
  }

  //  void
  //      QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::Element
  //      Type type)
  void handleSelectedElementChange(QtGraphs3D::ElementType type) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickGraphsItemCall60 call = reinterpret_cast<CuteQQuickGraphsItemCall60>(taken[60]);
      call(this, static_cast<int>(type), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSelectedElementChange(type);
  }

  //  void QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::Optim
  //      izationHint hint)
  void handleOptimizationHintChange(
      QtGraphs3D::OptimizationHint hint) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQuickGraphsItemCall61 call = reinterpret_cast<CuteQQuickGraphsItemCall61>(taken[61]);
      call(this, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleOptimizationHintChange(hint);
  }

  //  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickGraphsItemCall62 call = reinterpret_cast<CuteQQuickGraphsItemCall62>(taken[62]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::keyPressEvent(ev);
  }

  //  void QQuickGraphsItem::handleThemeTypeChange()
  void handleThemeTypeChange() override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickGraphsItemCall63 call = reinterpret_cast<CuteQQuickGraphsItemCall63>(taken[63]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleThemeTypeChange();
  }

  //  void QQuickGraphsItem::handleParentWidthChange()
  void handleParentWidthChange() override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickGraphsItemCall64 call = reinterpret_cast<CuteQQuickGraphsItemCall64>(taken[64]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentWidthChange();
  }

  //  void QQuickGraphsItem::handleParentHeightChange()
  void handleParentHeightChange() override {
    if (taken[65]) {
      int handled = 0;
      CuteQQuickGraphsItemCall65 call = reinterpret_cast<CuteQQuickGraphsItemCall65>(taken[65]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentHeightChange();
  }

  //  void QQuickGraphsItem::componentComplete()
  void componentComplete() override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickGraphsItemCall66 call = reinterpret_cast<CuteQQuickGraphsItemCall66>(taken[66]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::componentComplete();
  }

  //  void QQuickGraphsItem::createSliceView()
  void createSliceView() override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickGraphsItemCall67 call = reinterpret_cast<CuteQQuickGraphsItemCall67>(taken[67]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::createSliceView();
  }

  //  void QQuickGraphsItem::calculateSceneScalingFactors()
  void calculateSceneScalingFactors() override {
    if (taken[68]) {
      int handled = 0;
      CuteQQuickGraphsItemCall68 call = reinterpret_cast<CuteQQuickGraphsItemCall68>(taken[68]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QVector3D
  //      QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis
  //      *axis, QVector3D labelPosition, int index)
  QVector3D calculateCategoryLabelPosition(
      QAbstract3DAxis *axis,
      QVector3D labelPosition,
      int index) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQuickGraphsItemCall69 call = reinterpret_cast<CuteQQuickGraphsItemCall69>(taken[69]);
      const QVector3D * given = call(this, axis, &labelPosition, index, &handled);
      if (handled && given) return *given;
    }
    return QQuickGraphsItem::calculateCategoryLabelPosition(axis, labelPosition, index);
  }

  //  float
  //      QQuickGraphsItem::calculateCategoryGridLinePosition(QAbstract3DAx
  //      is *axis, int index)
  float calculateCategoryGridLinePosition(
      QAbstract3DAxis *axis,
      int index) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQuickGraphsItemCall70 call = reinterpret_cast<CuteQQuickGraphsItemCall70>(taken[70]);
      float given = call(this, axis, index, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::calculateCategoryGridLinePosition(axis, index);
  }

  //  void QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void updateShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQuickGraphsItemCall71 call = reinterpret_cast<CuteQQuickGraphsItemCall71>(taken[71]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateShadowQuality(quality);
  }

  //  void QQuickGraphsItem::updateSliceItemLabel(const QString &label,
  //      QVector3D position)
  void updateSliceItemLabel(
      const QString &label,
      QVector3D position) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQuickGraphsItemCall72 call = reinterpret_cast<CuteQQuickGraphsItemCall72>(taken[72]);
      call(this, &label, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSliceItemLabel(label, position);
  }

  //  void QQuickGraphsItem::synchData()
  void synchData() override {
    if (taken[73]) {
      int handled = 0;
      CuteQQuickGraphsItemCall73 call = reinterpret_cast<CuteQQuickGraphsItemCall73>(taken[73]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::synchData();
  }

  //  void QQuickGraphsItem::updateGraph()
  void updateGraph() override {
    if (taken[74]) {
      int handled = 0;
      CuteQQuickGraphsItemCall74 call = reinterpret_cast<CuteQQuickGraphsItemCall74>(taken[74]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateGraph();
  }

  //  void QQuickGraphsItem::toggleSliceGraph()
  void toggleSliceGraph() override {
    if (taken[75]) {
      int handled = 0;
      CuteQQuickGraphsItemCall75 call = reinterpret_cast<CuteQQuickGraphsItemCall75>(taken[75]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::toggleSliceGraph();
  }

  //  void QQuickGraphsItem::updateAxisRange(float min, float max)
  void updateAxisRange(float min, float max) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQuickGraphsItemCall76 call = reinterpret_cast<CuteQQuickGraphsItemCall76>(taken[76]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateAxisRange(min, max);
  }

  //  void QQuickGraphsItem::updateAxisReversed(bool enable)
  void updateAxisReversed(bool enable) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQuickGraphsItemCall77 call = reinterpret_cast<CuteQQuickGraphsItemCall77>(taken[77]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateAxisReversed(enable);
  }

  //  void QQuickGraphsItem::updateSingleHighlightColor()
  void updateSingleHighlightColor() override {
    if (taken[78]) {
      int handled = 0;
      CuteQQuickGraphsItemCall78 call = reinterpret_cast<CuteQQuickGraphsItemCall78>(taken[78]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSingleHighlightColor();
  }

  //  void QQuickGraphsItem::updateLightStrength()
  void updateLightStrength() override {
    if (taken[79]) {
      int handled = 0;
      CuteQQuickGraphsItemCall79 call = reinterpret_cast<CuteQQuickGraphsItemCall79>(taken[79]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateLightStrength();
  }

  //  void QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater
  //      *repeater, QColor axisLabelColor)
  void handleLabelCountChanged(
      QQuick3DRepeater *repeater,
      QColor axisLabelColor) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQuickGraphsItemCall80 call = reinterpret_cast<CuteQQuickGraphsItemCall80>(taken[80]);
      call(this, repeater, &axisLabelColor, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleLabelCountChanged(repeater, axisLabelColor);
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsItem::getSeriesMultiAxis(QAbstract3DSeries *series,
  //      QAbstract3DAxis::AxisOrientation orientation)
  QAbstract3DAxis *getSeriesMultiAxis(
      QAbstract3DSeries *series,
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQuickGraphsItemCall81 call = reinterpret_cast<CuteQQuickGraphsItemCall81>(taken[81]);
      void * given = call(this, series, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return {};
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsItem::createDefaultAxis(QAbstract3DAxis::AxisOrienta
  //      tion orientation)
  QAbstract3DAxis *createDefaultAxis(
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQuickGraphsItemCall82 call = reinterpret_cast<CuteQQuickGraphsItemCall82>(taken[82]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::createDefaultAxis(orientation);
  }

  //  void QQuickGraphsItem::startRecordingRemovesAndInserts()
  void startRecordingRemovesAndInserts() override {
    if (taken[83]) {
      int handled = 0;
      CuteQQuickGraphsItemCall83 call = reinterpret_cast<CuteQQuickGraphsItemCall83>(taken[83]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::startRecordingRemovesAndInserts();
  }

  //  bool QQuick3DViewport::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[84]) {
      int handled = 0;
      CuteQQuickGraphsItemCall84 call = reinterpret_cast<CuteQQuickGraphsItemCall84>(taken[84]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DViewport::isTextureProvider();
  }

  //  QSGTextureProvider *QQuick3DViewport::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[85]) {
      int handled = 0;
      CuteQQuickGraphsItemCall85 call = reinterpret_cast<CuteQQuickGraphsItemCall85>(taken[85]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuick3DViewport::textureProvider();
  }

  //  void QQuick3DViewport::releaseResources()
  void releaseResources() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQuickGraphsItemCall86 call = reinterpret_cast<CuteQQuickGraphsItemCall86>(taken[86]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DViewport::releaseResources();
  }

  //  QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQuickGraphsItemCall87 call = reinterpret_cast<CuteQQuickGraphsItemCall87>(taken[87]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuick3DViewport::updatePaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[88]) {
      int handled = 0;
      CuteQQuickGraphsItemCall88 call = reinterpret_cast<CuteQQuickGraphsItemCall88>(taken[88]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[89]) {
      int handled = 0;
      CuteQQuickGraphsItemCall89 call = reinterpret_cast<CuteQQuickGraphsItemCall89>(taken[89]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[90]) {
      int handled = 0;
      CuteQQuickGraphsItemCall90 call = reinterpret_cast<CuteQQuickGraphsItemCall90>(taken[90]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[91]) {
      int handled = 0;
      CuteQQuickGraphsItemCall91 call = reinterpret_cast<CuteQQuickGraphsItemCall91>(taken[91]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[92]) {
      int handled = 0;
      CuteQQuickGraphsItemCall92 call = reinterpret_cast<CuteQQuickGraphsItemCall92>(taken[92]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQuickGraphsItemCall93 call = reinterpret_cast<CuteQQuickGraphsItemCall93>(taken[93]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQuickGraphsItemCall94 call = reinterpret_cast<CuteQQuickGraphsItemCall94>(taken[94]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQuickGraphsItemCall95 call = reinterpret_cast<CuteQQuickGraphsItemCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQuickGraphsItemCall96 call = reinterpret_cast<CuteQQuickGraphsItemCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQuickGraphsItemCall97 call = reinterpret_cast<CuteQQuickGraphsItemCall97>(taken[97]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQuickGraphsItemCall98 call = reinterpret_cast<CuteQQuickGraphsItemCall98>(taken[98]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQuickGraphsItemCall99 call = reinterpret_cast<CuteQQuickGraphsItemCall99>(taken[99]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQuickGraphsItemCall100 call = reinterpret_cast<CuteQQuickGraphsItemCall100>(taken[100]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQuickGraphsItemCall101 call = reinterpret_cast<CuteQQuickGraphsItemCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[102]) {
      int handled = 0;
      CuteQQuickGraphsItemCall102 call = reinterpret_cast<CuteQQuickGraphsItemCall102>(taken[102]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQuickGraphsItemCall103 call = reinterpret_cast<CuteQQuickGraphsItemCall103>(taken[103]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQuickGraphsItemCall104 call = reinterpret_cast<CuteQQuickGraphsItemCall104>(taken[104]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQuickGraphsItemCall105 call = reinterpret_cast<CuteQQuickGraphsItemCall105>(taken[105]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQuickGraphsItemCall106 call = reinterpret_cast<CuteQQuickGraphsItemCall106>(taken[106]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQuickGraphsItemCall107 call = reinterpret_cast<CuteQQuickGraphsItemCall107>(taken[107]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQuickGraphsItemCall108 call = reinterpret_cast<CuteQQuickGraphsItemCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQuickGraphsItemCall109 call = reinterpret_cast<CuteQQuickGraphsItemCall109>(taken[109]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQuickGraphsItemCall110 call = reinterpret_cast<CuteQQuickGraphsItemCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQuickGraphsItemCall111 call = reinterpret_cast<CuteQQuickGraphsItemCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQuickGraphsItemCall112 call = reinterpret_cast<CuteQQuickGraphsItemCall112>(taken[112]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[113]) {
      int handled = 0;
      CuteQQuickGraphsItemCall113 call = reinterpret_cast<CuteQQuickGraphsItemCall113>(taken[113]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQuickGraphsItemCall114 call = reinterpret_cast<CuteQQuickGraphsItemCall114>(taken[114]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQuickGraphsItemCall115 call = reinterpret_cast<CuteQQuickGraphsItemCall115>(taken[115]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQuickGraphsItemCall116 call = reinterpret_cast<CuteQQuickGraphsItemCall116>(taken[116]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQuickGraphsItemCall117 call = reinterpret_cast<CuteQQuickGraphsItemCall117>(taken[117]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQuickGraphsItemCall118 call = reinterpret_cast<CuteQQuickGraphsItemCall118>(taken[118]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQuickGraphsItemCall119 call = reinterpret_cast<CuteQQuickGraphsItemCall119>(taken[119]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickGraphsItem10metaObjectEv(
    const QQuickGraphsItem *self) {
  return self->metaObject();
}

//  void *QQuickGraphsItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickGraphsItem11qt_metacastEPKc(
    QQuickGraphsItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QQuickGraphsItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickGraphsItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsItem::tr(s, c, n));
}

//  void QQuickGraphsItem::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24qt_qmlMarker_uncreatableEv(
    QQuickGraphsItem *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickGraphsItem::~QQuickGraphsItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItemD1Ev(QQuickGraphsItem *self) {
  delete self;
}

//  void QQuickGraphsItem::markDataDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13markDataDirtyEv(QQuickGraphsItem *self) {
  self->markDataDirty();
}

//  void QQuickGraphsItem::markSeriesVisualsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22markSeriesVisualsDirtyEv(
    QQuickGraphsItem *self) {
  self->markSeriesVisualsDirty();
}

//  void QQuickGraphsItem::markSeriesItemLabelsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem25markSeriesItemLabelsDirtyEv(
    QQuickGraphsItem *self) {
  self->markSeriesItemLabelsDirty();
}

//  void QQuickGraphsItem::emitNeedRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14emitNeedRenderEv(QQuickGraphsItem *self) {
  self->emitNeedRender();
}

//  void QQuickGraphsItem::setQueriedGraphPosition(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23setQueriedGraphPositionE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *position) {
  self->setQueriedGraphPosition(*position);
}

//  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisTitleChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisLabelsChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisSegmentCountChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisSubSegmentCountChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisAutoAdjustRangeChangedInOrientation(QAbs
//      tract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsItem *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisLabelFormatChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisReversedChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisFormatterDirtyBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisLabelAutoRotationChangedBySender(sender);
}

//  void
//      QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisScaleLabelsByCountChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisLabelSizeChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisTitleVisibilityChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisLabelVisibilityChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisTitleFixedChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleAxisTitleOffsetChangedBySender(sender);
}

//  void QQuickGraphsItem::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->handleSeriesVisibilityChangedBySender(sender);
}

//  void QQuickGraphsItem::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem25handleLightingModeChangedEv(
    QQuickGraphsItem *self) {
  self->handleLightingModeChanged();
}

//  void QQuickGraphsItem::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16adjustAxisRangesEv(
    QQuickGraphsItem *self) {
  self->adjustAxisRanges();
}

//  void QQuickGraphsItem::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->handleMultiAxisChanged(axis);
}

//  void QQuickGraphsItem::handleMultiAxisDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20handleMultiAxisDirtyEv(
    QQuickGraphsItem *self) {
  self->handleMultiAxisDirty();
}

//  bool QQuickGraphsItem::graphPositionQueryPending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem25graphPositionQueryPendingEv(
    const QQuickGraphsItem *self) {
  return self->graphPositionQueryPending();
}

//  void QQuickGraphsItem::setGraphPositionQueryPending(const bool &pending)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28setGraphPositionQueryPendingERKb(
    QQuickGraphsItem *self,
    bool pending) {
  self->setGraphPositionQueryPending(pending);
}

//  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series) {
  self->addSeriesInternal(series);
}

//  void QQuickGraphsItem::insertSeries(qsizetype index, QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12insertSeriesExP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    qsizetype index,
    QAbstract3DSeries *series) {
  self->insertSeries(index, series);
}

//  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series) {
  self->removeSeriesInternal(series);
}

//  QList<QAbstract3DSeries *> QQuickGraphsItem::seriesList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DSeries *> *ritual_ZN16QQuickGraphsItem10seriesListEv(
    QQuickGraphsItem *self) {
  return new QList<QAbstract3DSeries *>(self->seriesList());
}

//  void QQuickGraphsItem::setAxisX(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8setAxisXEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstract3DAxis *QQuickGraphsItem::axisX() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK16QQuickGraphsItem5axisXEv(
    const QQuickGraphsItem *self) {
  return self->axisX();
}

//  void QQuickGraphsItem::setAxisY(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8setAxisYEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstract3DAxis *QQuickGraphsItem::axisY() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK16QQuickGraphsItem5axisYEv(
    const QQuickGraphsItem *self) {
  return self->axisY();
}

//  void QQuickGraphsItem::setAxisZ(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8setAxisZEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QAbstract3DAxis *QQuickGraphsItem::axisZ() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK16QQuickGraphsItem5axisZEv(
    const QQuickGraphsItem *self) {
  return self->axisZ();
}

//  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->addAxis(axis);
}

//  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QAbstract3DAxis *> QQuickGraphsItem::axes() const
extern "C" Q_DECL_EXPORT
QList<QAbstract3DAxis *> *ritual_ZNK16QQuickGraphsItem4axesEv(
    const QQuickGraphsItem *self) {
  return new QList<QAbstract3DAxis *>(self->axes());
}

//  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13RenderingModeE(
    QQuickGraphsItem *self,
    QtGraphs3D::RenderingMode mode) {
  self->setRenderingMode(mode);
}

//  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::RenderingMode ritual_ZNK16QQuickGraphsItem13renderingModeEv(
    const QQuickGraphsItem *self) {
  return self->renderingMode();
}

//  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::TransparencyT
//      echnique technique)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE(
    QQuickGraphsItem *self,
    QtGraphs3D::TransparencyTechnique technique) {
  self->setTransparencyTechnique(technique);
}

//  QtGraphs3D::TransparencyTechnique
//      QQuickGraphsItem::transparencyTechnique() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::TransparencyTechnique ritual_ZNK16QQuickGraphsItem21transparencyTechniqueEv(
    const QQuickGraphsItem *self) {
  return self->transparencyTechnique();
}

//  void QQuickGraphsItem::setSelectionMode(QtGraphs3D::SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsItem *self,
    int mode) {
  self->setSelectionMode(QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsItem13selectionModeEv(
    const QQuickGraphsItem *self) {
  return static_cast<int>(self->selectionMode().toInt());
}

//  void QQuickGraphsItem::doSetShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18doSetShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->doSetShadowQuality(quality);
}

//  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->setShadowQuality(quality);
}

//  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ShadowQuality ritual_ZNK16QQuickGraphsItem13shadowQualityEv(
    const QQuickGraphsItem *self) {
  return self->shadowQuality();
}

//  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ElementType ritual_ZNK16QQuickGraphsItem15selectedElementEv(
    const QQuickGraphsItem *self) {
  return self->selectedElement();
}

//  void QQuickGraphsItem::setMsaaSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14setMsaaSamplesEi(
    QQuickGraphsItem *self,
    int samples) {
  self->setMsaaSamples(samples);
}

//  int QQuickGraphsItem::msaaSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsItem11msaaSamplesEv(
    const QQuickGraphsItem *self) {
  return self->msaaSamples();
}

//  void QQuickGraphsItem::addTheme(QGraphsTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8addThemeEP12QGraphsTheme(
    QQuickGraphsItem *self,
    QGraphsTheme *theme) {
  self->addTheme(theme);
}

//  void QQuickGraphsItem::releaseTheme(QGraphsTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12releaseThemeEP12QGraphsTheme(
    QQuickGraphsItem *self,
    QGraphsTheme *theme) {
  self->releaseTheme(theme);
}

//  void QQuickGraphsItem::setTheme(QGraphsTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8setThemeEP12QGraphsTheme(
    QQuickGraphsItem *self,
    QGraphsTheme *theme) {
  self->setTheme(theme);
}

//  QGraphsTheme *QQuickGraphsItem::theme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZNK16QQuickGraphsItem5themeEv(
    const QQuickGraphsItem *self) {
  return self->theme();
}

//  QList<QGraphsTheme *> QQuickGraphsItem::themes() const
extern "C" Q_DECL_EXPORT
QList<QGraphsTheme *> *ritual_ZNK16QQuickGraphsItem6themesEv(
    const QQuickGraphsItem *self) {
  return new QList<QGraphsTheme *>(self->themes());
}

//  bool QQuickGraphsItem::isSlicingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem15isSlicingActiveEv(
    const QQuickGraphsItem *self) {
  return self->isSlicingActive();
}

//  void QQuickGraphsItem::setSlicingActive(bool isSlicing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16setSlicingActiveEb(
    QQuickGraphsItem *self,
    bool isSlicing) {
  self->setSlicingActive(isSlicing);
}

//  bool QQuickGraphsItem::isCustomDataDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem17isCustomDataDirtyEv(
    const QQuickGraphsItem *self) {
  return self->isCustomDataDirty();
}

//  void QQuickGraphsItem::setCustomDataDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setCustomDataDirtyEb(
    QQuickGraphsItem *self,
    bool dirty) {
  self->setCustomDataDirty(dirty);
}

//  bool QQuickGraphsItem::isCustomItemDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem17isCustomItemDirtyEv(
    const QQuickGraphsItem *self) {
  return self->isCustomItemDirty();
}

//  void QQuickGraphsItem::setCustomItemDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setCustomItemDirtyEb(
    QQuickGraphsItem *self,
    bool dirty) {
  self->setCustomItemDirty(dirty);
}

//  bool QQuickGraphsItem::isCustomLabelItem(QCustom3DItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem17isCustomLabelItemEP13QCustom3DItem(
    const QQuickGraphsItem *self,
    QCustom3DItem *item) {
  return self->isCustomLabelItem(item);
}

//  bool QQuickGraphsItem::isCustomVolumeItem(QCustom3DItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem18isCustomVolumeItemEP13QCustom3DItem(
    const QQuickGraphsItem *self,
    QCustom3DItem *item) {
  return self->isCustomVolumeItem(item);
}

//  QImage QQuickGraphsItem::customTextureImage(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QQuickGraphsItem18customTextureImageEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  return new QImage(self->customTextureImage(item));
}

//  Q3DScene *QQuickGraphsItem::scene()
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZN16QQuickGraphsItem5sceneEv(QQuickGraphsItem *self) {
  return self->scene();
}

//  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series) {
  return self->hasSeries(series);
}

//  void QQuickGraphsItem::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14clearSelectionEv(QQuickGraphsItem *self) {
  self->clearSelection();
}

//  void QQuickGraphsItem::deleteCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17deleteCustomItemsEv(
    QQuickGraphsItem *self) {
  self->deleteCustomItems();
}

//  void QQuickGraphsItem::deleteCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16deleteCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  self->deleteCustomItem(item);
}

//  void QQuickGraphsItem::deleteCustomItem(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16deleteCustomItemE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *position) {
  self->deleteCustomItem(*position);
}

//  QList<QCustom3DItem *> QQuickGraphsItem::customItems() const
extern "C" Q_DECL_EXPORT
QList<QCustom3DItem *> *ritual_ZNK16QQuickGraphsItem11customItemsEv(
    const QQuickGraphsItem *self) {
  return new QList<QCustom3DItem *>(self->customItems());
}

//  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  return self->addCustomItem(item);
}

//  void QQuickGraphsItem::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17removeCustomItemsEv(
    QQuickGraphsItem *self) {
  self->removeCustomItems();
}

//  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  self->removeCustomItem(item);
}

//  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *position) {
  self->removeCustomItemAt(*position);
}

//  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  self->releaseCustomItem(item);
}

//  int QQuickGraphsItem::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsItem18selectedLabelIndexEv(
    const QQuickGraphsItem *self) {
  return self->selectedLabelIndex();
}

//  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK16QQuickGraphsItem12selectedAxisEv(
    const QQuickGraphsItem *self) {
  return self->selectedAxis();
}

//  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv(
    const QQuickGraphsItem *self) {
  return self->selectedCustomItemIndex();
}

//  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK16QQuickGraphsItem18selectedCustomItemEv(
    const QQuickGraphsItem *self) {
  return self->selectedCustomItem();
}

//  void
//      QQuickGraphsItem::appendCustomItemFunc(QQmlListProperty<QCustom3DItem
//      > *list, QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20appendCustomItemFuncEP16QQmlListPropertyI13QCustom3DItemEPS1_(
    QQmlListProperty<QCustom3DItem> *list,
    QCustom3DItem *item) {
  QQuickGraphsItem::appendCustomItemFunc(list, item);
}

//  qsizetype
//      QQuickGraphsItem::countCustomItemFunc(QQmlListProperty<QCustom3DItem>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN16QQuickGraphsItem19countCustomItemFuncEP16QQmlListPropertyI13QCustom3DItemE(
    QQmlListProperty<QCustom3DItem> *list) {
  return QQuickGraphsItem::countCustomItemFunc(list);
}

//  QCustom3DItem
//      *QQuickGraphsItem::atCustomItemFunc(QQmlListProperty<QCustom3DItem>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZN16QQuickGraphsItem16atCustomItemFuncEP16QQmlListPropertyI13QCustom3DItemEx(
    QQmlListProperty<QCustom3DItem> *list,
    qsizetype index) {
  return QQuickGraphsItem::atCustomItemFunc(list, index);
}

//  void
//      QQuickGraphsItem::clearCustomItemFunc(QQmlListProperty<QCustom3DItem>
//      *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19clearCustomItemFuncEP16QQmlListPropertyI13QCustom3DItemE(
    QQmlListProperty<QCustom3DItem> *list) {
  QQuickGraphsItem::clearCustomItemFunc(list);
}

//  void QQuickGraphsItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14geometryChangeERK6QRectFS2_(
    QQuickGraphsItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickGraphsItem::resizeViewports(QSizeF viewportSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15resizeViewportsE6QSizeF(
    QQuickGraphsItem *self,
    const QSizeF *viewportSize) {
  self->resizeViewports(*viewportSize);
}

//  void QQuickGraphsItem::checkWindowList(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15checkWindowListEP12QQuickWindow(
    QQuickGraphsItem *self,
    QQuickWindow *window) {
  self->checkWindowList(window);
}

//  void QQuickGraphsItem::setMeasureFps(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13setMeasureFpsEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setMeasureFps(enable);
}

//  bool QQuickGraphsItem::measureFps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem10measureFpsEv(
    const QQuickGraphsItem *self) {
  return self->measureFps();
}

//  int QQuickGraphsItem::currentFps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsItem10currentFpsEv(
    const QQuickGraphsItem *self) {
  return self->currentFps();
}

//  void QQuickGraphsItem::setOrthoProjection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setOrthoProjectionEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setOrthoProjection(enable);
}

//  bool QQuickGraphsItem::isOrthoProjection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem17isOrthoProjectionEv(
    const QQuickGraphsItem *self) {
  return self->isOrthoProjection();
}

//  void QQuickGraphsItem::setAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14setAspectRatioEd(
    QQuickGraphsItem *self,
    qreal ratio) {
  self->setAspectRatio(ratio);
}

//  qreal QQuickGraphsItem::aspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsItem11aspectRatioEv(
    const QQuickGraphsItem *self) {
  return self->aspectRatio();
}

//  void QQuickGraphsItem::setOptimizationHint(QtGraphs3D::OptimizationHint
//      hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19setOptimizationHintEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsItem *self,
    QtGraphs3D::OptimizationHint hint) {
  self->setOptimizationHint(hint);
}

//  QtGraphs3D::OptimizationHint QQuickGraphsItem::optimizationHint() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::OptimizationHint ritual_ZNK16QQuickGraphsItem16optimizationHintEv(
    const QQuickGraphsItem *self) {
  return self->optimizationHint();
}

//  void QQuickGraphsItem::setPolar(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8setPolarEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setPolar(enable);
}

//  bool QQuickGraphsItem::isPolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem7isPolarEv(const QQuickGraphsItem *self) {
  return self->isPolar();
}

//  void QQuickGraphsItem::setLabelMargin(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14setLabelMarginEf(
    QQuickGraphsItem *self,
    float offset) {
  self->setLabelMargin(offset);
}

//  float QQuickGraphsItem::labelMargin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem11labelMarginEv(
    const QQuickGraphsItem *self) {
  return self->labelMargin();
}

//  void QQuickGraphsItem::setRadialLabelOffset(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20setRadialLabelOffsetEf(
    QQuickGraphsItem *self,
    float offset) {
  self->setRadialLabelOffset(offset);
}

//  float QQuickGraphsItem::radialLabelOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem17radialLabelOffsetEv(
    const QQuickGraphsItem *self) {
  return self->radialLabelOffset();
}

//  void QQuickGraphsItem::setHorizontalAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24setHorizontalAspectRatioEd(
    QQuickGraphsItem *self,
    qreal ratio) {
  self->setHorizontalAspectRatio(ratio);
}

//  qreal QQuickGraphsItem::horizontalAspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsItem21horizontalAspectRatioEv(
    const QQuickGraphsItem *self) {
  return self->horizontalAspectRatio();
}

//  void QQuickGraphsItem::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem9setLocaleERK7QLocale(
    QQuickGraphsItem *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QQuickGraphsItem::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK16QQuickGraphsItem6localeEv(
    const QQuickGraphsItem *self) {
  return new QLocale(self->locale());
}

//  QVector3D QQuickGraphsItem::queriedGraphPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem20queriedGraphPositionEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->queriedGraphPosition());
}

//  void QQuickGraphsItem::setMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem9setMarginEd(
    QQuickGraphsItem *self,
    qreal margin) {
  self->setMargin(margin);
}

//  qreal QQuickGraphsItem::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsItem6marginEv(const QQuickGraphsItem *self) {
  return self->margin();
}

//  void QQuickGraphsItem::setCutoffMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15setCutoffMarginEd(
    QQuickGraphsItem *self,
    qreal margin) {
  self->setCutoffMargin(margin);
}

//  qreal QQuickGraphsItem::cutoffMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsItem12cutoffMarginEv(
    const QQuickGraphsItem *self) {
  return self->cutoffMargin();
}

//  bool QQuickGraphsItem::isReady()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem7isReadyEv(QQuickGraphsItem *self) {
  return self->isReady();
}

//  QQuick3DNode *QQuickGraphsItem::rootNode() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK16QQuickGraphsItem8rootNodeEv(
    const QQuickGraphsItem *self) {
  return self->rootNode();
}

//  QQuick3DNode *QQuickGraphsItem::cameraTarget()
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN16QQuickGraphsItem12cameraTargetEv(
    QQuickGraphsItem *self) {
  return self->cameraTarget();
}

//  void QQuickGraphsItem::setCameraTarget(QQuick3DNode *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15setCameraTargetEP12QQuick3DNode(
    QQuickGraphsItem *self,
    QQuick3DNode *target) {
  self->setCameraTarget(target);
}

//  QQuick3DModel *QQuickGraphsItem::background() const
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZNK16QQuickGraphsItem10backgroundEv(
    const QQuickGraphsItem *self) {
  return self->background();
}

//  void QQuickGraphsItem::setBackground(QQuick3DModel *newBackground)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13setBackgroundEP13QQuick3DModel(
    QQuickGraphsItem *self,
    QQuick3DModel *newBackground) {
  self->setBackground(newBackground);
}

//  QQuick3DModel *QQuickGraphsItem::backgroundBB() const
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZNK16QQuickGraphsItem12backgroundBBEv(
    const QQuickGraphsItem *self) {
  return self->backgroundBB();
}

//  QQuick3DDirectionalLight *QQuickGraphsItem::light() const
extern "C" Q_DECL_EXPORT
QQuick3DDirectionalLight *ritual_ZNK16QQuickGraphsItem5lightEv(
    const QQuickGraphsItem *self) {
  return self->light();
}

//  QQuick3DCustomMaterial *QQuickGraphsItem::createQmlCustomMaterial(const
//      QString &fileName)
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial *ritual_ZN16QQuickGraphsItem23createQmlCustomMaterialERK7QString(
    QQuickGraphsItem *self,
    const QString *fileName) {
  return self->createQmlCustomMaterial(*fileName);
}

//  QQuick3DPrincipledMaterial *QQuickGraphsItem::createPrincipledMaterial()
extern "C" Q_DECL_EXPORT
QQuick3DPrincipledMaterial *ritual_ZN16QQuickGraphsItem24createPrincipledMaterialEv(
    QQuickGraphsItem *self) {
  return self->createPrincipledMaterial();
}

//  QQuickItem *QQuickGraphsItem::itemLabel()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN16QQuickGraphsItem9itemLabelEv(QQuickGraphsItem *self) {
  return self->itemLabel();
}

//  QQuick3DNode *QQuickGraphsItem::sliceItemLabel()
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN16QQuickGraphsItem14sliceItemLabelEv(
    QQuickGraphsItem *self) {
  return self->sliceItemLabel();
}

//  QQuick3DRepeater *QQuickGraphsItem::repeaterX() const
extern "C" Q_DECL_EXPORT
QQuick3DRepeater *ritual_ZNK16QQuickGraphsItem9repeaterXEv(
    const QQuickGraphsItem *self) {
  return self->repeaterX();
}

//  QQuick3DRepeater *QQuickGraphsItem::repeaterY() const
extern "C" Q_DECL_EXPORT
QQuick3DRepeater *ritual_ZNK16QQuickGraphsItem9repeaterYEv(
    const QQuickGraphsItem *self) {
  return self->repeaterY();
}

//  QQuick3DRepeater *QQuickGraphsItem::repeaterZ() const
extern "C" Q_DECL_EXPORT
QQuick3DRepeater *ritual_ZNK16QQuickGraphsItem9repeaterZEv(
    const QQuickGraphsItem *self) {
  return self->repeaterZ();
}

//  QQuick3DNode *QQuickGraphsItem::titleLabelX() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK16QQuickGraphsItem11titleLabelXEv(
    const QQuickGraphsItem *self) {
  return self->titleLabelX();
}

//  QQuick3DNode *QQuickGraphsItem::titleLabelY() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK16QQuickGraphsItem11titleLabelYEv(
    const QQuickGraphsItem *self) {
  return self->titleLabelY();
}

//  QQuick3DNode *QQuickGraphsItem::titleLabelZ() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK16QQuickGraphsItem11titleLabelZEv(
    const QQuickGraphsItem *self) {
  return self->titleLabelZ();
}

//  bool QQuickGraphsItem::isXFlipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem10isXFlippedEv(
    const QQuickGraphsItem *self) {
  return self->isXFlipped();
}

//  void QQuickGraphsItem::setXFlipped(bool xFlipped)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11setXFlippedEb(
    QQuickGraphsItem *self,
    bool xFlipped) {
  self->setXFlipped(xFlipped);
}

//  bool QQuickGraphsItem::isYFlipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem10isYFlippedEv(
    const QQuickGraphsItem *self) {
  return self->isYFlipped();
}

//  void QQuickGraphsItem::setYFlipped(bool yFlipped)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11setYFlippedEb(
    QQuickGraphsItem *self,
    bool yFlipped) {
  self->setYFlipped(yFlipped);
}

//  bool QQuickGraphsItem::isZFlipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem10isZFlippedEv(
    const QQuickGraphsItem *self) {
  return self->isZFlipped();
}

//  void QQuickGraphsItem::setZFlipped(bool zFlipped)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11setZFlippedEb(
    QQuickGraphsItem *self,
    bool zFlipped) {
  self->setZFlipped(zFlipped);
}

//  QVector3D QQuickGraphsItem::scaleWithBackground() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem19scaleWithBackgroundEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->scaleWithBackground());
}

//  QVector3D QQuickGraphsItem::backgroundScaleMargin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem21backgroundScaleMarginEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->backgroundScaleMargin());
}

//  void QQuickGraphsItem::setScaleWithBackground(QVector3D scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22setScaleWithBackgroundE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *scale) {
  self->setScaleWithBackground(*scale);
}

//  void QQuickGraphsItem::setBackgroundScaleMargin(QVector3D margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24setBackgroundScaleMarginE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *margin) {
  self->setBackgroundScaleMargin(*margin);
}

//  QVector3D QQuickGraphsItem::rotation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem8rotationEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->rotation());
}

//  void QQuickGraphsItem::setRotation(QVector3D rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11setRotationE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *rotation) {
  self->setRotation(*rotation);
}

//  QVector3D QQuickGraphsItem::scale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem5scaleEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->scale());
}

//  void QQuickGraphsItem::setScale(QVector3D scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem8setScaleE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *scale) {
  self->setScale(*scale);
}

//  QVector3D QQuickGraphsItem::translate() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem9translateEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->translate());
}

//  void QQuickGraphsItem::setTranslate(QVector3D translate)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12setTranslateE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *translate) {
  self->setTranslate(*translate);
}

//  float QQuickGraphsItem::lineLengthScaleFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem21lineLengthScaleFactorEv(
    const QQuickGraphsItem *self) {
  return self->lineLengthScaleFactor();
}

//  void QQuickGraphsItem::setLineLengthScaleFactor(float scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24setLineLengthScaleFactorEf(
    QQuickGraphsItem *self,
    float scaleFactor) {
  self->setLineLengthScaleFactor(scaleFactor);
}

//  float QQuickGraphsItem::lineWidthScaleFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem20lineWidthScaleFactorEv(
    const QQuickGraphsItem *self) {
  return self->lineWidthScaleFactor();
}

//  void QQuickGraphsItem::setLineWidthScaleFactor(float scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23setLineWidthScaleFactorEf(
    QQuickGraphsItem *self,
    float scaleFactor) {
  self->setLineWidthScaleFactor(scaleFactor);
}

//  float QQuickGraphsItem::gridOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem10gridOffsetEv(
    const QQuickGraphsItem *self) {
  return self->gridOffset();
}

//  QtGraphs3D::CameraPreset QQuickGraphsItem::cameraPreset() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::CameraPreset ritual_ZNK16QQuickGraphsItem12cameraPresetEv(
    const QQuickGraphsItem *self) {
  return self->cameraPreset();
}

//  void QQuickGraphsItem::setCameraPreset(QtGraphs3D::CameraPreset preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15setCameraPresetEN10QtGraphs3D12CameraPresetE(
    QQuickGraphsItem *self,
    QtGraphs3D::CameraPreset preset) {
  self->setCameraPreset(preset);
}

//  float QQuickGraphsItem::cameraXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem15cameraXRotationEv(
    const QQuickGraphsItem *self) {
  return self->cameraXRotation();
}

//  void QQuickGraphsItem::setCameraXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setCameraXRotationEf(
    QQuickGraphsItem *self,
    float rotation) {
  self->setCameraXRotation(rotation);
}

//  float QQuickGraphsItem::cameraYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem15cameraYRotationEv(
    const QQuickGraphsItem *self) {
  return self->cameraYRotation();
}

//  void QQuickGraphsItem::setCameraYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setCameraYRotationEf(
    QQuickGraphsItem *self,
    float rotation) {
  self->setCameraYRotation(rotation);
}

//  float QQuickGraphsItem::minCameraXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem18minCameraXRotationEv(
    const QQuickGraphsItem *self) {
  return self->minCameraXRotation();
}

//  void QQuickGraphsItem::setMinCameraXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21setMinCameraXRotationEf(
    QQuickGraphsItem *self,
    float rotation) {
  self->setMinCameraXRotation(rotation);
}

//  float QQuickGraphsItem::maxCameraXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem18maxCameraXRotationEv(
    const QQuickGraphsItem *self) {
  return self->maxCameraXRotation();
}

//  void QQuickGraphsItem::setMaxCameraXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21setMaxCameraXRotationEf(
    QQuickGraphsItem *self,
    float rotation) {
  self->setMaxCameraXRotation(rotation);
}

//  float QQuickGraphsItem::minCameraYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem18minCameraYRotationEv(
    const QQuickGraphsItem *self) {
  return self->minCameraYRotation();
}

//  void QQuickGraphsItem::setMinCameraYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21setMinCameraYRotationEf(
    QQuickGraphsItem *self,
    float rotation) {
  self->setMinCameraYRotation(rotation);
}

//  float QQuickGraphsItem::maxCameraYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem18maxCameraYRotationEv(
    const QQuickGraphsItem *self) {
  return self->maxCameraYRotation();
}

//  void QQuickGraphsItem::setMaxCameraYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21setMaxCameraYRotationEf(
    QQuickGraphsItem *self,
    float rotation) {
  self->setMaxCameraYRotation(rotation);
}

//  void QQuickGraphsItem::setZoomAtTargetEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22setZoomAtTargetEnabledEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setZoomAtTargetEnabled(enable);
}

//  bool QQuickGraphsItem::zoomAtTargetEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem19zoomAtTargetEnabledEv(
    QQuickGraphsItem *self) {
  return self->zoomAtTargetEnabled();
}

//  void QQuickGraphsItem::setZoomEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14setZoomEnabledEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setZoomEnabled(enable);
}

//  bool QQuickGraphsItem::zoomEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem11zoomEnabledEv(QQuickGraphsItem *self) {
  return self->zoomEnabled();
}

//  void QQuickGraphsItem::setSelectionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19setSelectionEnabledEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setSelectionEnabled(enable);
}

//  bool QQuickGraphsItem::selectionEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem16selectionEnabledEv(
    QQuickGraphsItem *self) {
  return self->selectionEnabled();
}

//  void QQuickGraphsItem::setRotationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setRotationEnabledEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setRotationEnabled(enable);
}

//  bool QQuickGraphsItem::rotationEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem15rotationEnabledEv(QQuickGraphsItem *self) {
  return self->rotationEnabled();
}

//  void QQuickGraphsItem::setPanEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13setPanEnabledEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setPanEnabled(enable);
}

//  bool QQuickGraphsItem::panEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem10panEnabledEv(QQuickGraphsItem *self) {
  return self->panEnabled();
}

//  void QQuickGraphsItem::setDragMode(QtGraphs3D::DragMode newDragMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11setDragModeEN10QtGraphs3D8DragModeE(
    QQuickGraphsItem *self,
    QtGraphs3D::DragMode newDragMode) {
  self->setDragMode(newDragMode);
}

//  QtGraphs3D::DragMode QQuickGraphsItem::dragMode() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::DragMode ritual_ZNK16QQuickGraphsItem8dragModeEv(
    const QQuickGraphsItem *self) {
  return self->dragMode();
}

//  void QQuickGraphsItem::setDefaultInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22setDefaultInputHandlerEv(
    QQuickGraphsItem *self) {
  self->setDefaultInputHandler();
}

//  void QQuickGraphsItem::unsetDefaultInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24unsetDefaultInputHandlerEv(
    QQuickGraphsItem *self) {
  self->unsetDefaultInputHandler();
}

//  void QQuickGraphsItem::unsetDefaultTapHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22unsetDefaultTapHandlerEv(
    QQuickGraphsItem *self) {
  self->unsetDefaultTapHandler();
}

//  void QQuickGraphsItem::unsetDefaultDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23unsetDefaultDragHandlerEv(
    QQuickGraphsItem *self) {
  self->unsetDefaultDragHandler();
}

//  void QQuickGraphsItem::unsetDefaultWheelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24unsetDefaultWheelHandlerEv(
    QQuickGraphsItem *self) {
  self->unsetDefaultWheelHandler();
}

//  void QQuickGraphsItem::unsetDefaultPinchHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24unsetDefaultPinchHandlerEv(
    QQuickGraphsItem *self) {
  self->unsetDefaultPinchHandler();
}

//  void QQuickGraphsItem::setDragButton(Qt::MouseButtons button)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13setDragButtonE6QFlagsIN2Qt11MouseButtonEE(
    QQuickGraphsItem *self,
    int button) {
  self->setDragButton(QFlags<Qt::MouseButton>::fromInt(button));
}

//  void QQuickGraphsItem::setPanButton(Qt::MouseButtons button)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12setPanButtonE6QFlagsIN2Qt11MouseButtonEE(
    QQuickGraphsItem *self,
    int button) {
  self->setPanButton(QFlags<Qt::MouseButton>::fromInt(button));
}

//  float QQuickGraphsItem::cameraZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem15cameraZoomLevelEv(
    const QQuickGraphsItem *self) {
  return self->cameraZoomLevel();
}

//  void QQuickGraphsItem::setCameraZoomLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18setCameraZoomLevelEf(
    QQuickGraphsItem *self,
    float level) {
  self->setCameraZoomLevel(level);
}

//  float QQuickGraphsItem::minCameraZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem18minCameraZoomLevelEv(
    const QQuickGraphsItem *self) {
  return self->minCameraZoomLevel();
}

//  void QQuickGraphsItem::setMinCameraZoomLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21setMinCameraZoomLevelEf(
    QQuickGraphsItem *self,
    float level) {
  self->setMinCameraZoomLevel(level);
}

//  float QQuickGraphsItem::maxCameraZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem18maxCameraZoomLevelEv(
    const QQuickGraphsItem *self) {
  return self->maxCameraZoomLevel();
}

//  void QQuickGraphsItem::setMaxCameraZoomLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21setMaxCameraZoomLevelEf(
    QQuickGraphsItem *self,
    float level) {
  self->setMaxCameraZoomLevel(level);
}

//  void QQuickGraphsItem::setCameraTargetPosition(QVector3D target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23setCameraTargetPositionE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *target) {
  self->setCameraTargetPosition(*target);
}

//  QVector3D QQuickGraphsItem::cameraTargetPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsItem20cameraTargetPositionEv(
    const QQuickGraphsItem *self) {
  return new QVector3D(self->cameraTargetPosition());
}

//  bool QQuickGraphsItem::wrapCameraXRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem19wrapCameraXRotationEv(
    const QQuickGraphsItem *self) {
  return self->wrapCameraXRotation();
}

//  void QQuickGraphsItem::setWrapCameraXRotation(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22setWrapCameraXRotationEb(
    QQuickGraphsItem *self,
    bool wrap) {
  self->setWrapCameraXRotation(wrap);
}

//  bool QQuickGraphsItem::wrapCameraYRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem19wrapCameraYRotationEv(
    const QQuickGraphsItem *self) {
  return self->wrapCameraYRotation();
}

//  void QQuickGraphsItem::setWrapCameraYRotation(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22setWrapCameraYRotationEb(
    QQuickGraphsItem *self,
    bool wrap) {
  self->setWrapCameraYRotation(wrap);
}

//  QVector3D QQuickGraphsItem::graphPositionAt(QPoint point)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN16QQuickGraphsItem15graphPositionAtE6QPoint(
    QQuickGraphsItem *self,
    const QPoint *point) {
  return new QVector3D(self->graphPositionAt(*point));
}

//  void QQuickGraphsItem::setCameraPosition(float horizontal, float
//      vertical, float zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17setCameraPositionEfff(
    QQuickGraphsItem *self,
    float horizontal,
    float vertical,
    float zoom) {
  self->setCameraPosition(horizontal, vertical, zoom);
}

//  void QQuickGraphsItem::changeLabelBackgroundColor(QQuick3DRepeater
//      *repeater, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26changeLabelBackgroundColorEP16QQuick3DRepeater6QColor(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    const QColor *color) {
  self->changeLabelBackgroundColor(repeater, *color);
}

//  void QQuickGraphsItem::changeLabelBackgroundVisible(QQuick3DRepeater
//      *repeater, const bool &visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28changeLabelBackgroundVisibleEP16QQuick3DRepeaterRKb(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    bool visible) {
  self->changeLabelBackgroundVisible(repeater, visible);
}

//  void QQuickGraphsItem::changeLabelBorderVisible(QQuick3DRepeater
//      *repeater, const bool &visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24changeLabelBorderVisibleEP16QQuick3DRepeaterRKb(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    bool visible) {
  self->changeLabelBorderVisible(repeater, visible);
}

//  void QQuickGraphsItem::changeLabelTextColor(QQuick3DRepeater *repeater,
//      QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20changeLabelTextColorEP16QQuick3DRepeater6QColor(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    const QColor *color) {
  self->changeLabelTextColor(repeater, *color);
}

//  void QQuickGraphsItem::changeLabelFont(QQuick3DRepeater *repeater, const
//      QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15changeLabelFontEP16QQuick3DRepeaterRK5QFont(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    const QFont *font) {
  self->changeLabelFont(repeater, *font);
}

//  void QQuickGraphsItem::changeLabelsVisible(QQuick3DRepeater *repeater,
//      const bool &visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19changeLabelsVisibleEP16QQuick3DRepeaterRKb(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    bool visible) {
  self->changeLabelsVisible(repeater, visible);
}

//  void QQuickGraphsItem::changeGridLineColor(QQuick3DRepeater *repeater,
//      QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19changeGridLineColorEP16QQuick3DRepeater6QColor(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    const QColor *color) {
  self->changeGridLineColor(repeater, *color);
}

//  void QQuickGraphsItem::updateTitleLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17updateTitleLabelsEv(
    QQuickGraphsItem *self) {
  self->updateTitleLabels();
}

//  void QQuickGraphsItem::updateSelectionMode(QtGraphs3D::SelectionFlags
//      newMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsItem *self,
    int newMode) {
  self->updateSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(newMode));
}

//  void QQuickGraphsItem::setSliceActivatedChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24setSliceActivatedChangedEb(
    QQuickGraphsItem *self,
    bool changed) {
  self->setSliceActivatedChanged(changed);
}

//  bool QQuickGraphsItem::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem9doPickingE7QPointF(
    QQuickGraphsItem *self,
    const QPointF *point) {
  return self->doPicking(*point);
}

//  bool QQuickGraphsItem::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_(
    QQuickGraphsItem *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  void QQuickGraphsItem::minimizeMainGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17minimizeMainGraphEv(
    QQuickGraphsItem *self) {
  self->minimizeMainGraph();
}

//  int QQuickGraphsItem::horizontalFlipFactor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsItem20horizontalFlipFactorEv(
    const QQuickGraphsItem *self) {
  return self->horizontalFlipFactor();
}

//  void QQuickGraphsItem::setHorizontalFlipFactor(int
//      newHorizontalFlipFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23setHorizontalFlipFactorEi(
    QQuickGraphsItem *self,
    int newHorizontalFlipFactor) {
  self->setHorizontalFlipFactor(newHorizontalFlipFactor);
}

//  float QQuickGraphsItem::ambientLightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem20ambientLightStrengthEv(
    const QQuickGraphsItem *self) {
  return self->ambientLightStrength();
}

//  void QQuickGraphsItem::setAmbientLightStrength(float
//      newAmbientLightStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23setAmbientLightStrengthEf(
    QQuickGraphsItem *self,
    float newAmbientLightStrength) {
  self->setAmbientLightStrength(newAmbientLightStrength);
}

//  float QQuickGraphsItem::lightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem13lightStrengthEv(
    const QQuickGraphsItem *self) {
  return self->lightStrength();
}

//  void QQuickGraphsItem::setLightStrength(float newLightStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16setLightStrengthEf(
    QQuickGraphsItem *self,
    float newLightStrength) {
  self->setLightStrength(newLightStrength);
}

//  float QQuickGraphsItem::shadowStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsItem14shadowStrengthEv(
    const QQuickGraphsItem *self) {
  return self->shadowStrength();
}

//  void QQuickGraphsItem::setShadowStrength(float newShadowStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17setShadowStrengthEf(
    QQuickGraphsItem *self,
    float newShadowStrength) {
  self->setShadowStrength(newShadowStrength);
}

//  QColor QQuickGraphsItem::lightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickGraphsItem10lightColorEv(
    const QQuickGraphsItem *self) {
  return new QColor(self->lightColor());
}

//  void QQuickGraphsItem::setLightColor(QColor newLightColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13setLightColorE6QColor(
    QQuickGraphsItem *self,
    const QColor *newLightColor) {
  self->setLightColor(*newLightColor);
}

//  QtGraphs3D::GridLineType QQuickGraphsItem::gridLineType() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::GridLineType ritual_ZNK16QQuickGraphsItem12gridLineTypeEv(
    const QQuickGraphsItem *self) {
  return self->gridLineType();
}

//  void QQuickGraphsItem::setGridLineType(const QtGraphs3D::GridLineType
//      &gridLineType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15setGridLineTypeERKN10QtGraphs3D12GridLineTypeE(
    QQuickGraphsItem *self,
    const QtGraphs3D::GridLineType *gridLineType) {
  self->setGridLineType(*gridLineType);
}

//  void QQuickGraphsItem::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void QQuickGraphsItem::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void QQuickGraphsItem::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  void QQuickGraphsItem::handleFpsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16handleFpsChangedEv(
    QQuickGraphsItem *self) {
  self->handleFpsChanged();
}

//  void QQuickGraphsItem::windowDestroyed(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15windowDestroyedEP7QObject(
    QQuickGraphsItem *self,
    QObject *obj) {
  self->windowDestroyed(obj);
}

//  void QQuickGraphsItem::handleAxisTitleChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22handleAxisTitleChangedERK7QString(
    QQuickGraphsItem *self,
    const QString *title) {
  self->handleAxisTitleChanged(*title);
}

//  void QQuickGraphsItem::handleAxisLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23handleAxisLabelsChangedEv(
    QQuickGraphsItem *self) {
  self->handleAxisLabelsChanged();
}

//  void QQuickGraphsItem::handleAxisRangeChanged(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22handleAxisRangeChangedEff(
    QQuickGraphsItem *self,
    float min,
    float max) {
  self->handleAxisRangeChanged(min, max);
}

//  void QQuickGraphsItem::handleAxisSegmentCountChanged(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem29handleAxisSegmentCountChangedEx(
    QQuickGraphsItem *self,
    qsizetype count) {
  self->handleAxisSegmentCountChanged(count);
}

//  void QQuickGraphsItem::handleAxisSubSegmentCountChanged(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem32handleAxisSubSegmentCountChangedEx(
    QQuickGraphsItem *self,
    qsizetype count) {
  self->handleAxisSubSegmentCountChanged(count);
}

//  void QQuickGraphsItem::handleAxisAutoAdjustRangeChanged(bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem32handleAxisAutoAdjustRangeChangedEb(
    QQuickGraphsItem *self,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChanged(autoAdjust);
}

//  void QQuickGraphsItem::handleAxisScaleLabelsByCountChanged(bool adjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem35handleAxisScaleLabelsByCountChangedEb(
    QQuickGraphsItem *self,
    bool adjust) {
  self->handleAxisScaleLabelsByCountChanged(adjust);
}

//  void QQuickGraphsItem::handleAxisLabelSizeChanged(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26handleAxisLabelSizeChangedEd(
    QQuickGraphsItem *self,
    qreal size) {
  self->handleAxisLabelSizeChanged(size);
}

//  void QQuickGraphsItem::handleAxisLabelFormatChanged(const QString
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28handleAxisLabelFormatChangedERK7QString(
    QQuickGraphsItem *self,
    const QString *format) {
  self->handleAxisLabelFormatChanged(*format);
}

//  void QQuickGraphsItem::handleAxisReversedChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem25handleAxisReversedChangedEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->handleAxisReversedChanged(enable);
}

//  void QQuickGraphsItem::handleAxisFormatterDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24handleAxisFormatterDirtyEv(
    QQuickGraphsItem *self) {
  self->handleAxisFormatterDirty();
}

//  void QQuickGraphsItem::handleAxisLabelAutoRotationChanged(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem34handleAxisLabelAutoRotationChangedEf(
    QQuickGraphsItem *self,
    float angle) {
  self->handleAxisLabelAutoRotationChanged(angle);
}

//  void QQuickGraphsItem::handleAxisTitleVisibilityChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem32handleAxisTitleVisibilityChangedEb(
    QQuickGraphsItem *self,
    bool visible) {
  self->handleAxisTitleVisibilityChanged(visible);
}

//  void QQuickGraphsItem::handleAxisLabelVisibilityChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem32handleAxisLabelVisibilityChangedEb(
    QQuickGraphsItem *self,
    bool visible) {
  self->handleAxisLabelVisibilityChanged(visible);
}

//  void QQuickGraphsItem::handleAxisTitleFixedChanged(bool fixed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem27handleAxisTitleFixedChangedEb(
    QQuickGraphsItem *self,
    bool fixed) {
  self->handleAxisTitleFixedChanged(fixed);
}

//  void QQuickGraphsItem::handleAxisTitleOffsetChanged(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28handleAxisTitleOffsetChangedEf(
    QQuickGraphsItem *self,
    float offset) {
  self->handleAxisTitleOffsetChanged(offset);
}

//  void QQuickGraphsItem::handleInputPositionChanged(QPoint position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26handleInputPositionChangedE6QPoint(
    QQuickGraphsItem *self,
    const QPoint *position) {
  self->handleInputPositionChanged(*position);
}

//  void QQuickGraphsItem::handleSeriesVisibilityChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem29handleSeriesVisibilityChangedEb(
    QQuickGraphsItem *self,
    bool visible) {
  self->handleSeriesVisibilityChanged(visible);
}

//  void QQuickGraphsItem::handleItemLabelVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem29handleItemLabelVisibleChangedEb(
    QQuickGraphsItem *self,
    bool visible) {
  self->handleItemLabelVisibleChanged(visible);
}

//  void QQuickGraphsItem::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsItem *self,
    bool visible,
    QObject *sender) {
  self->handleItemLabelVisibleChangedBySender(visible, sender);
}

//  void
//      QQuickGraphsItem::handleThemeColorStyleChanged(QGraphsTheme::ColorSty
//      le style)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28handleThemeColorStyleChangedEN12QGraphsTheme10ColorStyleE(
    QQuickGraphsItem *self,
    QGraphsTheme::ColorStyle style) {
  self->handleThemeColorStyleChanged(style);
}

//  void QQuickGraphsItem::handleThemeBaseColorsChanged(const QList<QColor>
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28handleThemeBaseColorsChangedERK5QListI6QColorE(
    QQuickGraphsItem *self,
    const QList<QColor> *color) {
  self->handleThemeBaseColorsChanged(*color);
}

//  void QQuickGraphsItem::handleThemeBaseGradientsChanged(const
//      QList<QLinearGradient> &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem31handleThemeBaseGradientsChangedERK5QListI15QLinearGradientE(
    QQuickGraphsItem *self,
    const QList<QLinearGradient> *gradient) {
  self->handleThemeBaseGradientsChanged(*gradient);
}

//  void QQuickGraphsItem::handleThemeSingleHighlightColorChanged(QColor
//      color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem38handleThemeSingleHighlightColorChangedE6QColor(
    QQuickGraphsItem *self,
    const QColor *color) {
  self->handleThemeSingleHighlightColorChanged(*color);
}

//  void QQuickGraphsItem::handleThemeSingleHighlightGradientChanged(const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem41handleThemeSingleHighlightGradientChangedERK15QLinearGradient(
    QQuickGraphsItem *self,
    const QLinearGradient *gradient) {
  self->handleThemeSingleHighlightGradientChanged(*gradient);
}

//  void QQuickGraphsItem::handleThemeMultiHighlightColorChanged(QColor
//      color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem37handleThemeMultiHighlightColorChangedE6QColor(
    QQuickGraphsItem *self,
    const QColor *color) {
  self->handleThemeMultiHighlightColorChanged(*color);
}

//  void QQuickGraphsItem::handleThemeMultiHighlightGradientChanged(const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem40handleThemeMultiHighlightGradientChangedERK15QLinearGradient(
    QQuickGraphsItem *self,
    const QLinearGradient *gradient) {
  self->handleThemeMultiHighlightGradientChanged(*gradient);
}

//  void QQuickGraphsItem::handleThemeTypeChanged(QGraphsTheme::Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22handleThemeTypeChangedEN12QGraphsTheme5ThemeE(
    QQuickGraphsItem *self,
    QGraphsTheme::Theme theme) {
  self->handleThemeTypeChanged(theme);
}

//  void
//      QQuickGraphsItem::handleRequestShadowQuality(QtGraphs3D::ShadowQualit
//      y quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26handleRequestShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->handleRequestShadowQuality(quality);
}

//  void QQuickGraphsItem::updateCustomItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16updateCustomItemEv(
    QQuickGraphsItem *self) {
  self->updateCustomItem();
}

//  bool QQuickGraphsItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem5eventEP6QEvent(
    QQuickGraphsItem *self,
    QEvent *event) {
  return self->event(event);
}

//  void QQuickGraphsItem::setParentNode(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13setParentNodeEP12QQuick3DNode(
    QQuickGraphsItem *self,
    QQuick3DNode *node) {
  self->setParentNode(node);
}

//  void QQuickGraphsItem::handleWindowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19handleWindowChangedEv(
    QQuickGraphsItem *self) {
  self->handleWindowChanged();
}

//  void QQuickGraphsItem::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickGraphsItem *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickGraphsItem::updateWindowParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22updateWindowParametersEv(
    QQuickGraphsItem *self) {
  self->updateWindowParameters();
}

//  void
//      QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::SelectionFlag
//      s mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsItem *self,
    int mode) {
  self->handleSelectionModeChange(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void
//      QQuickGraphsItem::handleShadowQualityChange(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->handleShadowQualityChange(quality);
}

//  void
//      QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::ElementType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3D11ElementTypeE(
    QQuickGraphsItem *self,
    QtGraphs3D::ElementType type) {
  self->handleSelectedElementChange(type);
}

//  void QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::Optimizat
//      ionHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsItem *self,
    QtGraphs3D::OptimizationHint hint) {
  self->handleOptimizationHintChange(hint);
}

//  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem13keyPressEventEP9QKeyEvent(
    QQuickGraphsItem *self,
    QKeyEvent *ev) {
  self->keyPressEvent(ev);
}

//  void QQuickGraphsItem::handleThemeTypeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21handleThemeTypeChangeEv(
    QQuickGraphsItem *self) {
  self->handleThemeTypeChange();
}

//  void QQuickGraphsItem::handleParentWidthChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23handleParentWidthChangeEv(
    QQuickGraphsItem *self) {
  self->handleParentWidthChange();
}

//  void QQuickGraphsItem::handleParentHeightChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem24handleParentHeightChangeEv(
    QQuickGraphsItem *self) {
  self->handleParentHeightChange();
}

//  void QQuickGraphsItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17componentCompleteEv(
    QQuickGraphsItem *self) {
  self->componentComplete();
}

//  void QQuickGraphsItem::checkSliceEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17checkSliceEnabledEv(
    QQuickGraphsItem *self) {
  self->checkSliceEnabled();
}

//  bool QQuickGraphsItem::isUserCameraRotationRange()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem25isUserCameraRotationRangeEv(
    QQuickGraphsItem *self) {
  return self->isUserCameraRotationRange();
}

//  void QQuickGraphsItem::setUserCameraRotationRange(bool userRotationRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26setUserCameraRotationRangeEb(
    QQuickGraphsItem *self,
    bool userRotationRange) {
  self->setUserCameraRotationRange(userRotationRange);
}

//  void QQuickGraphsItem::createSliceView()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15createSliceViewEv(QQuickGraphsItem *self) {
  self->createSliceView();
}

//  QQuick3DViewport
//      *QQuickGraphsItem::createOffscreenSliceView(QtGraphs3D::SliceCaptureT
//      ype sliceType)
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN16QQuickGraphsItem24createOffscreenSliceViewEN10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsItem *self,
    QtGraphs3D::SliceCaptureType sliceType) {
  return self->createOffscreenSliceView(sliceType);
}

//  void QQuickGraphsItem::handleGraphQueryPositionChanged(QPoint position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem31handleGraphQueryPositionChangedE6QPoint(
    QQuickGraphsItem *self,
    const QPoint *position) {
  self->handleGraphQueryPositionChanged(*position);
}

//  void QQuickGraphsItem::handleSelectionQueryPositionChanged(QPoint
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem35handleSelectionQueryPositionChangedE6QPoint(
    QQuickGraphsItem *self,
    const QPoint *position) {
  self->handleSelectionQueryPositionChanged(*position);
}

//  void QQuickGraphsItem::handlePrimarySubViewportChanged(const QRect rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem31handlePrimarySubViewportChangedE5QRect(
    QQuickGraphsItem *self,
    const QRect *rect) {
  self->handlePrimarySubViewportChanged(*rect);
}

//  void QQuickGraphsItem::handleSecondarySubViewportChanged(const QRect
//      rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem33handleSecondarySubViewportChangedE5QRect(
    QQuickGraphsItem *self,
    const QRect *rect) {
  self->handleSecondarySubViewportChanged(*rect);
}

//  QQuick3DNode *QQuickGraphsItem::graphNode()
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN16QQuickGraphsItem9graphNodeEv(
    QQuickGraphsItem *self) {
  return self->graphNode();
}

//  QQuick3DViewport *QQuickGraphsItem::sliceView()
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN16QQuickGraphsItem9sliceViewEv(
    QQuickGraphsItem *self) {
  return self->sliceView();
}

//  QQmlComponent *QQuickGraphsItem::createRepeaterDelegateComponent(const
//      QString &fileName)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN16QQuickGraphsItem31createRepeaterDelegateComponentERK7QString(
    QQuickGraphsItem *self,
    const QString *fileName) {
  return self->createRepeaterDelegateComponent(*fileName);
}

//  QQuick3DRepeater *QQuickGraphsItem::createRepeater(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRepeater *ritual_ZN16QQuickGraphsItem14createRepeaterEP12QQuick3DNode(
    QQuickGraphsItem *self,
    QQuick3DNode *parent) {
  return self->createRepeater(parent);
}

//  QQuick3DNode *QQuickGraphsItem::createTitleLabel(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN16QQuickGraphsItem16createTitleLabelEP12QQuick3DNode(
    QQuickGraphsItem *self,
    QQuick3DNode *parent) {
  return self->createTitleLabel(parent);
}

//  void QQuickGraphsItem::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15createItemLabelEv(QQuickGraphsItem *self) {
  self->createItemLabel();
}

//  void QQuickGraphsItem::updateXTitle(QVector3D labelRotation, QVector3D
//      labelTrans, const QQuaternion &totalRotation, float labelsMaxWidth,
//      QVector3D scale, QAbstract3DAxis *axis, QQuick3DNode *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12updateXTitleE9QVector3DS0_RK11QQuaternionfS0_P15QAbstract3DAxisP12QQuick3DNode(
    QQuickGraphsItem *self,
    const QVector3D *labelRotation,
    const QVector3D *labelTrans,
    const QQuaternion *totalRotation,
    float labelsMaxWidth,
    const QVector3D *scale,
    QAbstract3DAxis *axis,
    QQuick3DNode *label) {
  self->updateXTitle(
      *labelRotation,
      *labelTrans,
      *totalRotation,
      labelsMaxWidth,
      *scale,
      axis,
      label);
}

//  void QQuickGraphsItem::updateYTitle(QVector3D sideLabelRotation,
//      QVector3D backLabelRotation, QVector3D sideLabelTrans, QVector3D
//      backLabelTrans, const QQuaternion &totalSideRotation, const
//      QQuaternion &totalBackRotation, float labelsMaxWidth, QVector3D
//      scale, QAbstract3DAxis *axis, QQuick3DNode *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12updateYTitleE9QVector3DS0_S0_S0_RK11QQuaternionS3_fS0_P15QAbstract3DAxisP12QQuick3DNode(
    QQuickGraphsItem *self,
    const QVector3D *sideLabelRotation,
    const QVector3D *backLabelRotation,
    const QVector3D *sideLabelTrans,
    const QVector3D *backLabelTrans,
    const QQuaternion *totalSideRotation,
    const QQuaternion *totalBackRotation,
    float labelsMaxWidth,
    const QVector3D *scale,
    QAbstract3DAxis *axis,
    QQuick3DNode *label) {
  self->updateYTitle(
      *sideLabelRotation,
      *backLabelRotation,
      *sideLabelTrans,
      *backLabelTrans,
      *totalSideRotation,
      *totalBackRotation,
      labelsMaxWidth,
      *scale,
      axis,
      label);
}

//  void QQuickGraphsItem::updateZTitle(QVector3D labelRotation, QVector3D
//      labelTrans, const QQuaternion &totalRotation, float labelsMaxWidth,
//      QVector3D scale, QAbstract3DAxis *axis, QQuick3DNode *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12updateZTitleE9QVector3DS0_RK11QQuaternionfS0_P15QAbstract3DAxisP12QQuick3DNode(
    QQuickGraphsItem *self,
    const QVector3D *labelRotation,
    const QVector3D *labelTrans,
    const QQuaternion *totalRotation,
    float labelsMaxWidth,
    const QVector3D *scale,
    QAbstract3DAxis *axis,
    QQuick3DNode *label) {
  self->updateZTitle(
      *labelRotation,
      *labelTrans,
      *totalRotation,
      labelsMaxWidth,
      *scale,
      axis,
      label);
}

//  void QQuickGraphsItem::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv(
    QQuickGraphsItem *self) {
  self->calculateSceneScalingFactors();
}

//  void QQuickGraphsItem::positionAndScaleLine(QQuick3DNode *lineNode,
//      QVector3D scale, QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20positionAndScaleLineEP12QQuick3DNode9QVector3DS2_(
    QQuickGraphsItem *self,
    QQuick3DNode *lineNode,
    const QVector3D *scale,
    const QVector3D *position) {
  self->positionAndScaleLine(lineNode, *scale, *position);
}

//  int QQuickGraphsItem::findLabelsMaxWidth(const QStringList &labels)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickGraphsItem18findLabelsMaxWidthERK5QListI7QStringE(
    QQuickGraphsItem *self,
    const QList<QString> *labels) {
  return self->findLabelsMaxWidth(*labels);
}

//  QVector3D
//      QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis
//      *axis, QVector3D labelPosition, int index)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis,
    const QVector3D *labelPosition,
    int index) {
  return new QVector3D(
      self->calculateCategoryLabelPosition(
          axis,
          *labelPosition,
          index));
}

//  float QQuickGraphsItem::calculateCategoryGridLinePosition(QAbstract3DAxis
//      *axis, int index)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAbstract3DAxisi(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis,
    int index) {
  return self->calculateCategoryGridLinePosition(axis, index);
}

//  float QQuickGraphsItem::calculatePolarBackgroundMargin()
extern "C" Q_DECL_EXPORT
float ritual_ZN16QQuickGraphsItem30calculatePolarBackgroundMarginEv(
    QQuickGraphsItem *self) {
  return self->calculatePolarBackgroundMargin();
}

//  void QQuickGraphsItem::setFloorGridInRange(bool inRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19setFloorGridInRangeEb(
    QQuickGraphsItem *self,
    bool inRange) {
  self->setFloorGridInRange(inRange);
}

//  void QQuickGraphsItem::setVerticalSegmentLine(bool hasVerticalLine)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem22setVerticalSegmentLineEb(
    QQuickGraphsItem *self,
    bool hasVerticalLine) {
  self->setVerticalSegmentLine(hasVerticalLine);
}

//  void QQuickGraphsItem::updateGrid()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem10updateGridEv(QQuickGraphsItem *self) {
  self->updateGrid();
}

//  void QQuickGraphsItem::updateGridLineType()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18updateGridLineTypeEv(
    QQuickGraphsItem *self) {
  self->updateGridLineType();
}

//  void QQuickGraphsItem::updateLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12updateLabelsEv(QQuickGraphsItem *self) {
  self->updateLabels();
}

//  QVector3D QQuickGraphsItem::calculateLabelRotation(float labelAutoAngle,
//      float fractionCamX, float fractionCamY, Qt::Axis axis)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN16QQuickGraphsItem22calculateLabelRotationEfffN2Qt4AxisE(
    QQuickGraphsItem *self,
    float labelAutoAngle,
    float fractionCamX,
    float fractionCamY,
    Qt::Axis axis) {
  return new QVector3D(
      self->calculateLabelRotation(
          labelAutoAngle,
          fractionCamX,
          fractionCamY,
          axis));
}

//  void QQuickGraphsItem::updateSliceGrid(QQuick3DModel *sliceGrid,
//      QtGraphs3D::SliceCaptureType selectedFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15updateSliceGridEP13QQuick3DModelN10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsItem *self,
    QQuick3DModel *sliceGrid,
    QtGraphs3D::SliceCaptureType selectedFlag) {
  self->updateSliceGrid(sliceGrid, selectedFlag);
}

//  void QQuickGraphsItem::updateSliceLabels(QQuick3DRepeater
//      *horizontalLabel, QQuick3DRepeater *verticalLabel, QQuick3DNode
//      *horizontalTitle, QQuick3DNode *verticalTitle, QQuick3DNode
//      *itemLabel, QtGraphs3D::SliceCaptureType selectedFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17updateSliceLabelsEP16QQuick3DRepeaterS1_P12QQuick3DNodeS3_S3_N10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsItem *self,
    QQuick3DRepeater *horizontalLabel,
    QQuick3DRepeater *verticalLabel,
    QQuick3DNode *horizontalTitle,
    QQuick3DNode *verticalTitle,
    QQuick3DNode *itemLabel,
    QtGraphs3D::SliceCaptureType selectedFlag) {
  self->updateSliceLabels(
      horizontalLabel,
      verticalLabel,
      horizontalTitle,
      verticalTitle,
      itemLabel,
      selectedFlag);
}

//  void QQuickGraphsItem::updateBackgroundColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21updateBackgroundColorEv(
    QQuickGraphsItem *self) {
  self->updateBackgroundColor();
}

//  void QQuickGraphsItem::setItemSelected(bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15setItemSelectedEb(
    QQuickGraphsItem *self,
    bool selected) {
  self->setItemSelected(selected);
}

//  void QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->updateShadowQuality(quality);
}

//  void QQuickGraphsItem::updateItemLabel(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15updateItemLabelE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *position) {
  self->updateItemLabel(*position);
}

//  void QQuickGraphsItem::updateSliceItemLabel(const QString &label,
//      QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3D(
    QQuickGraphsItem *self,
    const QString *label,
    const QVector3D *position) {
  self->updateSliceItemLabel(*label, *position);
}

//  void QQuickGraphsItem::synchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem9synchDataEv(QQuickGraphsItem *self) {
  self->synchData();
}

//  void QQuickGraphsItem::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11updateGraphEv(QQuickGraphsItem *self) {
  self->updateGraph();
}

//  bool QQuickGraphsItem::isSliceEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem14isSliceEnabledEv(
    const QQuickGraphsItem *self) {
  return self->isSliceEnabled();
}

//  void QQuickGraphsItem::setSliceEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15setSliceEnabledEb(
    QQuickGraphsItem *self,
    bool enabled) {
  self->setSliceEnabled(enabled);
}

//  bool QQuickGraphsItem::isSliceActivatedChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem23isSliceActivatedChangedEv(
    const QQuickGraphsItem *self) {
  return self->isSliceActivatedChanged();
}

//  void QQuickGraphsItem::toggleSliceGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16toggleSliceGraphEv(
    QQuickGraphsItem *self) {
  self->toggleSliceGraph();
}

//  void QQuickGraphsItem::createSliceCamera(QQuick3DViewport *sliceView)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem17createSliceCameraEP16QQuick3DViewport(
    QQuickGraphsItem *self,
    QQuick3DViewport *sliceView) {
  self->createSliceCamera(sliceView);
}

//  bool QQuickGraphsItem::isSliceOrthoProjection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsItem22isSliceOrthoProjectionEv(
    const QQuickGraphsItem *self) {
  return self->isSliceOrthoProjection();
}

//  void QQuickGraphsItem::setSliceOrthoProjection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23setSliceOrthoProjectionEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->setSliceOrthoProjection(enable);
}

//  void QQuickGraphsItem::updateAxisRange(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15updateAxisRangeEff(
    QQuickGraphsItem *self,
    float min,
    float max) {
  self->updateAxisRange(min, max);
}

//  void QQuickGraphsItem::updateAxisReversed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem18updateAxisReversedEb(
    QQuickGraphsItem *self,
    bool enable) {
  self->updateAxisReversed(enable);
}

//  void QQuickGraphsItem::updateSingleHighlightColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26updateSingleHighlightColorEv(
    QQuickGraphsItem *self) {
  self->updateSingleHighlightColor();
}

//  void QQuickGraphsItem::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19updateLightStrengthEv(
    QQuickGraphsItem *self) {
  self->updateLightStrength();
}

//  void QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater
//      *repeater, QColor axisLabelColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepeater6QColor(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    const QColor *axisLabelColor) {
  self->handleLabelCountChanged(repeater, *axisLabelColor);
}

//  void QQuickGraphsItem::updateMultiAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem15updateMultiAxisEv(QQuickGraphsItem *self) {
  self->updateMultiAxis();
}

//  void QQuickGraphsItem::updateMultiAxisLabels(qsizetype axisIndex,
//      QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem21updateMultiAxisLabelsExP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    qsizetype axisIndex,
    QAbstract3DAxis *axis) {
  self->updateMultiAxisLabels(axisIndex, axis);
}

//  void QQuickGraphsItem::updateMultiAxisGrid(qsizetype axisIndex,
//      QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19updateMultiAxisGridExP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    qsizetype axisIndex,
    QAbstract3DAxis *axis) {
  self->updateMultiAxisGrid(axisIndex, axis);
}

//  void QQuickGraphsItem::releaseMultiAxis(QAbstract3DAxis::AxisOrientation
//      orientation, qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16releaseMultiAxisEN15QAbstract3DAxis15AxisOrientationEx(
    QQuickGraphsItem *self,
    QAbstract3DAxis::AxisOrientation orientation,
    qsizetype index) {
  self->releaseMultiAxis(orientation, index);
}

//  void QQuickGraphsItem::connectMultiAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16connectMultiAxisEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->connectMultiAxis(axis);
}

//  QAbstract3DAxis *QQuickGraphsItem::getSeriesMultiAxis(QAbstract3DSeries
//      *series, QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->getSeriesMultiAxis(series, orientation);
}

//  bool QQuickGraphsItem::isGridUpdated()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsItem13isGridUpdatedEv(QQuickGraphsItem *self) {
  return self->isGridUpdated();
}

//  void QQuickGraphsItem::setGridUpdated(bool updated)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14setGridUpdatedEb(
    QQuickGraphsItem *self,
    bool updated) {
  self->setGridUpdated(updated);
}

//  QGraphsInputHandler *QQuickGraphsItem::graphsInputHandler() const
extern "C" Q_DECL_EXPORT
QGraphsInputHandler *ritual_ZNK16QQuickGraphsItem18graphsInputHandlerEv(
    const QQuickGraphsItem *self) {
  return self->graphsInputHandler();
}

//  QAbstract3DAxis
//      *QQuickGraphsItem::createDefaultAxis(QAbstract3DAxis::AxisOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsItem *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  QValue3DAxis *QQuickGraphsItem::createDefaultValueAxis()
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZN16QQuickGraphsItem22createDefaultValueAxisEv(
    QQuickGraphsItem *self) {
  return self->createDefaultValueAxis();
}

//  QCategory3DAxis *QQuickGraphsItem::createDefaultCategoryAxis()
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZN16QQuickGraphsItem25createDefaultCategoryAxisEv(
    QQuickGraphsItem *self) {
  return self->createDefaultCategoryAxis();
}

//  void QQuickGraphsItem::startRecordingRemovesAndInserts()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv(
    QQuickGraphsItem *self) {
  self->startRecordingRemovesAndInserts();
}

//  void QQuickGraphsItem::setUpCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem11setUpCameraEv(QQuickGraphsItem *self) {
  self->setUpCamera();
}

//  void QQuickGraphsItem::setUpLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem10setUpLightEv(QQuickGraphsItem *self) {
  self->setUpLight();
}

//  void QQuickGraphsItem::updateCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem12updateCameraEv(QQuickGraphsItem *self) {
  self->updateCamera();
}

//  void QQuickGraphsItem::updateRadialLabelOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem23updateRadialLabelOffsetEv(
    QQuickGraphsItem *self) {
  self->updateRadialLabelOffset();
}

//  void QQuickGraphsItem::updateCustomData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem16updateCustomDataEv(
    QQuickGraphsItem *self) {
  self->updateCustomData();
}

//  void QQuickGraphsItem::updateCustomLabelsRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem26updateCustomLabelsRotationEv(
    QQuickGraphsItem *self) {
  self->updateCustomLabelsRotation();
}

//  float QQuickGraphsItem::fontScaleFactor(float pointSize)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QQuickGraphsItem15fontScaleFactorEf(
    QQuickGraphsItem *self,
    float pointSize) {
  return self->fontScaleFactor(pointSize);
}

//  float QQuickGraphsItem::labelAdjustment(float width)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QQuickGraphsItem15labelAdjustmentEf(
    QQuickGraphsItem *self,
    float width) {
  return self->labelAdjustment(width);
}

//  void QQuickGraphsItem::gridLineCountHelper(QAbstract3DAxis *axis,
//      qsizetype &lineCount, qsizetype &sublineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19gridLineCountHelperEP15QAbstract3DAxisRxS2_(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis,
    qsizetype *lineCount,
    qsizetype *sublineCount) {
  self->gridLineCountHelper(axis, *lineCount, *sublineCount);
}

//  QVector3D QQuickGraphsItem::graphPosToAbsolute(QVector3D position)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN16QQuickGraphsItem18graphPosToAbsoluteE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *position) {
  return new QVector3D(self->graphPosToAbsolute(*position));
}

//  void QQuickGraphsItem::createVolumeMaterial(QCustom3DVolume *volume,
//      Volume &volumeItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem20createVolumeMaterialEP15QCustom3DVolumeRNS_6VolumeE(
    QQuickGraphsItem *self,
    QCustom3DVolume *volume,
    QQuickGraphsItem::Volume *volumeItem) {
  self->createVolumeMaterial(volume, *volumeItem);
}

//  QQuick3DModel *QQuickGraphsItem::createSliceFrame(Volume &volumeItem)
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZN16QQuickGraphsItem16createSliceFrameERNS_6VolumeE(
    QQuickGraphsItem *self,
    QQuickGraphsItem::Volume *volumeItem) {
  return self->createSliceFrame(*volumeItem);
}

//  void QQuickGraphsItem::updateSliceFrameMaterials(QCustom3DVolume *volume,
//      Volume &volumeItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem25updateSliceFrameMaterialsEP15QCustom3DVolumeRNS_6VolumeE(
    QQuickGraphsItem *self,
    QCustom3DVolume *volume,
    QQuickGraphsItem::Volume *volumeItem) {
  self->updateSliceFrameMaterials(volume, *volumeItem);
}

//  void QQuickGraphsItem::updateSubViews()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem14updateSubViewsEv(QQuickGraphsItem *self) {
  self->updateSubViews();
}

//  void QQuickGraphsItem::updateCustomVolumes()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsItem19updateCustomVolumesEv(
    QQuickGraphsItem *self) {
  self->updateCustomVolumes();
}

//  a Python function taken by a CuteQQuickGraphsItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsItem(
    QQuickGraphsItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsItem *>(self)->take(key, call);
}

//  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisTitleChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisLabelsChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisSegmentCountChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisLabelFormatChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisReversedChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisFormatterDirtyBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(sender);
}

//  void
//      QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(
      sender);
}

//  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisLabelSizeChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisTitleFixedChangedBySender(sender);
}

//  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(sender);
}

//  void QQuickGraphsItem::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsItem *self,
    QObject *sender) {
  self->QQuickGraphsItem::handleSeriesVisibilityChangedBySender(sender);
}

//  void QQuickGraphsItem::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsItem::handleMultiAxisChanged(axis);
}

//  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series) {
  self->QQuickGraphsItem::addSeriesInternal(series);
}

//  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series) {
  self->QQuickGraphsItem::removeSeriesInternal(series);
}

//  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsItem::addAxis(axis);
}

//  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsItem::releaseAxis(axis);
}

//  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13RenderingModeE(
    QQuickGraphsItem *self,
    QtGraphs3D::RenderingMode mode) {
  self->QQuickGraphsItem::setRenderingMode(mode);
}

//  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::RenderingMode ritual_own_ZNK16QQuickGraphsItem13renderingModeEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::renderingMode();
}

//  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::TransparencyT
//      echnique technique)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE(
    QQuickGraphsItem *self,
    QtGraphs3D::TransparencyTechnique technique) {
  self->QQuickGraphsItem::setTransparencyTechnique(technique);
}

//  QtGraphs3D::TransparencyTechnique
//      QQuickGraphsItem::transparencyTechnique() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::TransparencyTechnique ritual_own_ZNK16QQuickGraphsItem21transparencyTechniqueEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::transparencyTechnique();
}

//  void QQuickGraphsItem::setSelectionMode(QtGraphs3D::SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsItem *self,
    int mode) {
  self->QQuickGraphsItem::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QQuickGraphsItem13selectionModeEv(
    const QQuickGraphsItem *self) {
  return static_cast<int>(self->QQuickGraphsItem::selectionMode().toInt());
}

//  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->QQuickGraphsItem::setShadowQuality(quality);
}

//  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ShadowQuality ritual_own_ZNK16QQuickGraphsItem13shadowQualityEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::shadowQuality();
}

//  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ElementType ritual_own_ZNK16QQuickGraphsItem15selectedElementEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::selectedElement();
}

//  void QQuickGraphsItem::setMsaaSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem14setMsaaSamplesEi(
    QQuickGraphsItem *self,
    int samples) {
  self->QQuickGraphsItem::setMsaaSamples(samples);
}

//  int QQuickGraphsItem::msaaSamples() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QQuickGraphsItem11msaaSamplesEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::msaaSamples();
}

//  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries(
    QQuickGraphsItem *self,
    QAbstract3DSeries *series) {
  return self->QQuickGraphsItem::hasSeries(series);
}

//  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  return self->QQuickGraphsItem::addCustomItem(item);
}

//  void QQuickGraphsItem::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem17removeCustomItemsEv(
    QQuickGraphsItem *self) {
  self->QQuickGraphsItem::removeCustomItems();
}

//  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  self->QQuickGraphsItem::removeCustomItem(item);
}

//  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D(
    QQuickGraphsItem *self,
    const QVector3D *position) {
  self->QQuickGraphsItem::removeCustomItemAt(*position);
}

//  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem(
    QQuickGraphsItem *self,
    QCustom3DItem *item) {
  self->QQuickGraphsItem::releaseCustomItem(item);
}

//  int QQuickGraphsItem::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QQuickGraphsItem18selectedLabelIndexEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::selectedLabelIndex();
}

//  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZNK16QQuickGraphsItem12selectedAxisEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::selectedAxis();
}

//  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::selectedCustomItemIndex();
}

//  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_own_ZNK16QQuickGraphsItem18selectedCustomItemEv(
    const QQuickGraphsItem *self) {
  return self->QQuickGraphsItem::selectedCustomItem();
}

//  void QQuickGraphsItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem14geometryChangeERK6QRectFS2_(
    QQuickGraphsItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->QQuickGraphsItem::geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickGraphsItem::updateSelectionMode(QtGraphs3D::SelectionFlags
//      newMode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsItem *self,
    int newMode) {
  self->QQuickGraphsItem::updateSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(newMode));
}

//  bool QQuickGraphsItem::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsItem9doPickingE7QPointF(
    QQuickGraphsItem *self,
    const QPointF *point) {
  return self->QQuickGraphsItem::doPicking(*point);
}

//  bool QQuickGraphsItem::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_(
    QQuickGraphsItem *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->QQuickGraphsItem::doRayPicking(*origin, *direction);
}

//  bool QQuickGraphsItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsItem5eventEP6QEvent(
    QQuickGraphsItem *self,
    QEvent *event) {
  return static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::event(
      event);
}

//  void QQuickGraphsItem::handleWindowChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem19handleWindowChangedEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleWindowChanged();
}

//  void QQuickGraphsItem::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickGraphsItem *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::itemChange(
      change,
      *value);
}

//  void QQuickGraphsItem::updateWindowParameters()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem22updateWindowParametersEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateWindowParameters();
}

//  void
//      QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::SelectionFlag
//      s mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsItem *self,
    int mode) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleSelectionModeChange(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void
//      QQuickGraphsItem::handleShadowQualityChange(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleShadowQualityChange(
      quality);
}

//  void
//      QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::ElementType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3D11ElementTypeE(
    QQuickGraphsItem *self,
    QtGraphs3D::ElementType type) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleSelectedElementChange(
      type);
}

//  void QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::Optimizat
//      ionHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsItem *self,
    QtGraphs3D::OptimizationHint hint) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleOptimizationHintChange(
      hint);
}

//  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem13keyPressEventEP9QKeyEvent(
    QQuickGraphsItem *self,
    QKeyEvent *ev) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::keyPressEvent(
      ev);
}

//  void QQuickGraphsItem::handleThemeTypeChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem21handleThemeTypeChangeEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleThemeTypeChange();
}

//  void QQuickGraphsItem::handleParentWidthChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem23handleParentWidthChangeEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleParentWidthChange();
}

//  void QQuickGraphsItem::handleParentHeightChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem24handleParentHeightChangeEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleParentHeightChange();
}

//  void QQuickGraphsItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem17componentCompleteEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::componentComplete();
}

//  void QQuickGraphsItem::createSliceView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem15createSliceViewEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::createSliceView();
}

//  QVector3D
//      QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis
//      *axis, QVector3D labelPosition, int index)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis,
    const QVector3D *labelPosition,
    int index) {
  return new QVector3D(
      static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::calculateCategoryLabelPosition(
          axis,
          *labelPosition,
          index));
}

//  float QQuickGraphsItem::calculateCategoryGridLinePosition(QAbstract3DAxis
//      *axis, int index)
extern "C" Q_DECL_EXPORT
float ritual_own_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAbstract3DAxisi(
    QQuickGraphsItem *self,
    QAbstract3DAxis *axis,
    int index) {
  return static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::calculateCategoryGridLinePosition(
      axis,
      index);
}

//  void QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsItem *self,
    QtGraphs3D::ShadowQuality quality) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateShadowQuality(
      quality);
}

//  void QQuickGraphsItem::updateSliceItemLabel(const QString &label,
//      QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3D(
    QQuickGraphsItem *self,
    const QString *label,
    const QVector3D *position) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateSliceItemLabel(
      *label,
      *position);
}

//  void QQuickGraphsItem::synchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem9synchDataEv(QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::synchData();
}

//  void QQuickGraphsItem::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem11updateGraphEv(QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateGraph();
}

//  void QQuickGraphsItem::toggleSliceGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem16toggleSliceGraphEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::toggleSliceGraph();
}

//  void QQuickGraphsItem::updateAxisRange(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem15updateAxisRangeEff(
    QQuickGraphsItem *self,
    float min,
    float max) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateAxisRange(
      min,
      max);
}

//  void QQuickGraphsItem::updateAxisReversed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem18updateAxisReversedEb(
    QQuickGraphsItem *self,
    bool enable) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateAxisReversed(
      enable);
}

//  void QQuickGraphsItem::updateSingleHighlightColor()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem26updateSingleHighlightColorEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateSingleHighlightColor();
}

//  void QQuickGraphsItem::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem19updateLightStrengthEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::updateLightStrength();
}

//  void QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater
//      *repeater, QColor axisLabelColor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepeater6QColor(
    QQuickGraphsItem *self,
    QQuick3DRepeater *repeater,
    const QColor *axisLabelColor) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::handleLabelCountChanged(
      repeater,
      *axisLabelColor);
}

//  QAbstract3DAxis
//      *QQuickGraphsItem::createDefaultAxis(QAbstract3DAxis::AxisOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsItem *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::createDefaultAxis(
      orientation);
}

//  void QQuickGraphsItem::startRecordingRemovesAndInserts()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv(
    QQuickGraphsItem *self) {
  static_cast<OwnQQuickGraphsItem *>(self)->OwnQQuickGraphsItem::startRecordingRemovesAndInserts();
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
