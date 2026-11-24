//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsbars_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphsbars_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtGraphs/qbar3dseries.h>
#include <QtCore/qurl.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickGraphsBars may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsBars : QQuickGraphsBars {
  using QQuickGraphsBars::componentComplete;
  using QQuickGraphsBars::synchData;
  using QQuickGraphsBars::updateGraph;
  using QQuickGraphsBars::updateAxisRange;
  using QQuickGraphsBars::updateAxisReversed;
  using QQuickGraphsBars::updateLightStrength;
  using QQuickGraphsBars::calculateSceneScalingFactors;
  using QQuickGraphsBars::calculateCategoryLabelPosition;
  using QQuickGraphsBars::calculateCategoryGridLinePosition;
  using QQuickGraphsBars::createSliceView;
  using QQuickGraphsBars::toggleSliceGraph;
  using QQuickGraphsBars::handleLabelCountChanged;
  using QQuickGraphsBars::updateSelectionMode;
  using QQuickGraphsBars::doPicking;
  using QQuickGraphsBars::doRayPicking;
  using QQuickGraphsBars::createDefaultAxis;
  using QQuickGraphsBars::updateSliceItemLabel;
  using QQuickGraphsBars::getSeriesMultiAxis;
};

//  A QQuickGraphsBars that Python can take functions over in. Every QQuickGraphsBars
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsBarsCall0)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall1)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall2)(const void *, int, bool, int *);
typedef void (*CuteQQuickGraphsBarsCall3)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall4)(const void *, bool, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall5)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall6)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall7)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall8)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsBarsCall9)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall10)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall11)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall12)(const void *, float, float, int *);
typedef void (*CuteQQuickGraphsBarsCall13)(const void *, bool, int *);
typedef void (*CuteQQuickGraphsBarsCall14)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall15)(const void *, int *);
typedef const QVector3D * (*CuteQQuickGraphsBarsCall16)(const void *, QAbstract3DAxis *, const QVector3D *, int, int *);
typedef float (*CuteQQuickGraphsBarsCall17)(const void *, QAbstract3DAxis *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall18)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall19)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall20)(const void *, QQuick3DRepeater *, const QColor *, int *);
typedef void (*CuteQQuickGraphsBarsCall21)(const void *, int, int *);
typedef bool (*CuteQQuickGraphsBarsCall22)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsBarsCall23)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void * (*CuteQQuickGraphsBarsCall24)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall25)(const void *, const QString *, const QVector3D *, int *);
typedef void * (*CuteQQuickGraphsBarsCall26)(const void *, QAbstract3DSeries *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall27)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsBarsCall28)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsBarsCall29)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsBarsCall30)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall31)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall32)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall33)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall34)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall35)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall36)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall37)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall38)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall39)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall40)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall41)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall42)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall43)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsBarsCall44)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsBarsCall45)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsBarsCall46)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsBarsCall47)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsBarsCall48)(const void *, int, int *);
typedef int (*CuteQQuickGraphsBarsCall49)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall50)(const void *, int, int *);
typedef int (*CuteQQuickGraphsBarsCall51)(const void *, int *);
typedef int (*CuteQQuickGraphsBarsCall52)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall53)(const void *, int, int *);
typedef int (*CuteQQuickGraphsBarsCall54)(const void *, int *);
typedef int (*CuteQQuickGraphsBarsCall55)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall56)(const void *, int, int *);
typedef int (*CuteQQuickGraphsBarsCall57)(const void *, int *);
typedef bool (*CuteQQuickGraphsBarsCall58)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsBarsCall59)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsBarsCall60)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall61)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsBarsCall62)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsBarsCall63)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsBarsCall64)(const void *, int *);
typedef void * (*CuteQQuickGraphsBarsCall65)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsBarsCall66)(const void *, int *);
typedef void * (*CuteQQuickGraphsBarsCall67)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall68)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsBarsCall69)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsCall70)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall71)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsBarsCall72)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall73)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall74)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall75)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall76)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall77)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall78)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall79)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall80)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall81)(const void *, int, int *);
typedef void (*CuteQQuickGraphsBarsCall82)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall83)(const void *, int *);
typedef bool (*CuteQQuickGraphsBarsCall84)(const void *, int *);
typedef void * (*CuteQQuickGraphsBarsCall85)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall86)(const void *, int *);
typedef void * (*CuteQQuickGraphsBarsCall87)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQQuickGraphsBarsCall88)(const void *, int *);
typedef const QRectF * (*CuteQQuickGraphsBarsCall89)(const void *, int *);
typedef bool (*CuteQQuickGraphsBarsCall90)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickGraphsBarsCall91)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsBarsCall92)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall93)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickGraphsBarsCall94)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsBarsCall95)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall96)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall97)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall98)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall99)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall100)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall101)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsCall102)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsBarsCall103)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsBarsCall104)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall105)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall106)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall107)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsBarsCall108)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsBarsCall109)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsBarsCall110)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsBarsCall111)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickGraphsBarsCall112)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickGraphsBarsCall113)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsBarsCall114)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsCall115)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsCall116)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsCall117)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsCall118)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsCall119)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsBars : public QQuickGraphsBars {
public:
  using QQuickGraphsBars::QQuickGraphsBars;
  void *taken[120] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14clearSelectionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7QObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySenderEbP7QObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16adjustAxisRangesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleLightingModeChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxis")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9synchDataEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11updateGraphEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15updateAxisRangeEff")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18updateAxisReversedEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateLightStrengthEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAbstract3DAxisi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15createSliceViewEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16toggleSliceGraphEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepeater6QColor")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9doPickingE7QPointF")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3D")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObject")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7QObject")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySenderEP7QObject")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7QObject")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObject")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObject")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySenderEP7QObject")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySenderEP7QObject")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QObject")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySenderEP7QObject")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySenderEP7QObject")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QObject")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7QObject")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSeries")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13RenderingModeE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13renderingModeEv")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem21transparencyTechniqueEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13selectionModeEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13shadowQualityEv")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem15selectedElementEv")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14setMsaaSamplesEi")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem11msaaSamplesEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17removeCustomItemsEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedLabelIndexEv")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem12selectedAxisEv")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedCustomItemEv")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[68] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[69] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19handleWindowChangedEv")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22updateWindowParametersEv")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D13ShadowQualityE")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3D11ElementTypeE")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem21handleThemeTypeChangeEv")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleParentWidthChangeEv")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24handleParentHeightChangeEv")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem26updateSingleHighlightColorEv")) {
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

  //  void QQuickGraphsBars::clearSelection()
  void clearSelection() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall0 call = reinterpret_cast<CuteQQuickGraphsBarsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::clearSelection();
  }

  //  void QQuickGraphsBars::setSelectionMode(QtGraphs3D::SelectionFlags
  //      mode)
  void setSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall1 call = reinterpret_cast<CuteQQuickGraphsBarsCall1>(taken[1]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsBars::setSelectionMode(mode);
  }

  //  void QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(
  //      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
  void handleAxisAutoAdjustRangeChangedInOrientation(
      QAbstract3DAxis::AxisOrientation orientation,
      bool autoAdjust) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall2 call = reinterpret_cast<CuteQQuickGraphsBarsCall2>(taken[2]);
      call(this, static_cast<int>(orientation), autoAdjust, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(orientation, autoAdjust);
  }

  //  void QQuickGraphsBars::handleSeriesVisibilityChangedBySender(QObject
  //      *sender)
  void handleSeriesVisibilityChangedBySender(QObject *sender) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall3 call = reinterpret_cast<CuteQQuickGraphsBarsCall3>(taken[3]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleSeriesVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsBars::handleItemLabelVisibleChangedBySender(bool
  //      visible, QObject *sender)
  void handleItemLabelVisibleChangedBySender(
      bool visible,
      QObject *sender) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall4 call = reinterpret_cast<CuteQQuickGraphsBarsCall4>(taken[4]);
      call(this, visible, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleItemLabelVisibleChangedBySender(visible, sender);
  }

  //  void QQuickGraphsBars::handleAxisRangeChangedBySender(QObject
  //      *sender)
  void handleAxisRangeChangedBySender(QObject *sender) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall5 call = reinterpret_cast<CuteQQuickGraphsBarsCall5>(taken[5]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleAxisRangeChangedBySender(sender);
  }

  //  void QQuickGraphsBars::adjustAxisRanges()
  void adjustAxisRanges() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall6 call = reinterpret_cast<CuteQQuickGraphsBarsCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::adjustAxisRanges();
  }

  //  void QQuickGraphsBars::handleLightingModeChanged()
  void handleLightingModeChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall7 call = reinterpret_cast<CuteQQuickGraphsBarsCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleLightingModeChanged();
  }

  //  void QQuickGraphsBars::handleMultiAxisChanged(QAbstract3DAxis *axis)
  void handleMultiAxisChanged(QAbstract3DAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall8 call = reinterpret_cast<CuteQQuickGraphsBarsCall8>(taken[8]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleMultiAxisChanged(axis);
  }

  //  void QQuickGraphsBars::componentComplete()
  void componentComplete() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall9 call = reinterpret_cast<CuteQQuickGraphsBarsCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::componentComplete();
  }

  //  void QQuickGraphsBars::synchData()
  void synchData() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall10 call = reinterpret_cast<CuteQQuickGraphsBarsCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::synchData();
  }

  //  void QQuickGraphsBars::updateGraph()
  void updateGraph() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall11 call = reinterpret_cast<CuteQQuickGraphsBarsCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::updateGraph();
  }

  //  void QQuickGraphsBars::updateAxisRange(float min, float max)
  void updateAxisRange(float min, float max) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall12 call = reinterpret_cast<CuteQQuickGraphsBarsCall12>(taken[12]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::updateAxisRange(min, max);
  }

  //  void QQuickGraphsBars::updateAxisReversed(bool enable)
  void updateAxisReversed(bool enable) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall13 call = reinterpret_cast<CuteQQuickGraphsBarsCall13>(taken[13]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::updateAxisReversed(enable);
  }

  //  void QQuickGraphsBars::updateLightStrength()
  void updateLightStrength() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall14 call = reinterpret_cast<CuteQQuickGraphsBarsCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::updateLightStrength();
  }

  //  void QQuickGraphsBars::calculateSceneScalingFactors()
  void calculateSceneScalingFactors() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall15 call = reinterpret_cast<CuteQQuickGraphsBarsCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::calculateSceneScalingFactors();
  }

  //  QVector3D
  //      QQuickGraphsBars::calculateCategoryLabelPosition(QAbstract3DAxis
  //      *axis, QVector3D labelPosition, int index)
  QVector3D calculateCategoryLabelPosition(
      QAbstract3DAxis *axis,
      QVector3D labelPosition,
      int index) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall16 call = reinterpret_cast<CuteQQuickGraphsBarsCall16>(taken[16]);
      const QVector3D * given = call(this, axis, &labelPosition, index, &handled);
      if (handled && given) return *given;
    }
    return QQuickGraphsBars::calculateCategoryLabelPosition(axis, labelPosition, index);
  }

  //  float
  //      QQuickGraphsBars::calculateCategoryGridLinePosition(QAbstract3DAx
  //      is *axis, int index)
  float calculateCategoryGridLinePosition(
      QAbstract3DAxis *axis,
      int index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall17 call = reinterpret_cast<CuteQQuickGraphsBarsCall17>(taken[17]);
      float given = call(this, axis, index, &handled);
      if (handled) return given;
    }
    return QQuickGraphsBars::calculateCategoryGridLinePosition(axis, index);
  }

  //  void QQuickGraphsBars::createSliceView()
  void createSliceView() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall18 call = reinterpret_cast<CuteQQuickGraphsBarsCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::createSliceView();
  }

  //  void QQuickGraphsBars::toggleSliceGraph()
  void toggleSliceGraph() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall19 call = reinterpret_cast<CuteQQuickGraphsBarsCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::toggleSliceGraph();
  }

  //  void QQuickGraphsBars::handleLabelCountChanged(QQuick3DRepeater
  //      *repeater, QColor axisLabelColor)
  void handleLabelCountChanged(
      QQuick3DRepeater *repeater,
      QColor axisLabelColor) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall20 call = reinterpret_cast<CuteQQuickGraphsBarsCall20>(taken[20]);
      call(this, repeater, &axisLabelColor, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleLabelCountChanged(repeater, axisLabelColor);
  }

  //  void QQuickGraphsBars::updateSelectionMode(QtGraphs3D::SelectionFlags
  //      mode)
  void updateSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall21 call = reinterpret_cast<CuteQQuickGraphsBarsCall21>(taken[21]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsBars::updateSelectionMode(mode);
  }

  //  bool QQuickGraphsBars::doPicking(QPointF position)
  bool doPicking(QPointF position) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall22 call = reinterpret_cast<CuteQQuickGraphsBarsCall22>(taken[22]);
      bool given = call(this, &position, &handled);
      if (handled) return given;
    }
    return QQuickGraphsBars::doPicking(position);
  }

  //  bool QQuickGraphsBars::doRayPicking(QVector3D origin, QVector3D
  //      direction)
  bool doRayPicking(QVector3D origin, QVector3D direction) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall23 call = reinterpret_cast<CuteQQuickGraphsBarsCall23>(taken[23]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsBars::doRayPicking(origin, direction);
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsBars::createDefaultAxis(QAbstract3DAxis::AxisOrienta
  //      tion orientation)
  QAbstract3DAxis *createDefaultAxis(
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall24 call = reinterpret_cast<CuteQQuickGraphsBarsCall24>(taken[24]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsBars::createDefaultAxis(orientation);
  }

  //  void QQuickGraphsBars::updateSliceItemLabel(const QString &label,
  //      QVector3D position)
  void updateSliceItemLabel(
      const QString &label,
      QVector3D position) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall25 call = reinterpret_cast<CuteQQuickGraphsBarsCall25>(taken[25]);
      call(this, &label, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::updateSliceItemLabel(label, position);
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsBars::getSeriesMultiAxis(QAbstract3DSeries *series,
  //      QAbstract3DAxis::AxisOrientation orientation)
  QAbstract3DAxis *getSeriesMultiAxis(
      QAbstract3DSeries *series,
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall26 call = reinterpret_cast<CuteQQuickGraphsBarsCall26>(taken[26]);
      void * given = call(this, series, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsBars::getSeriesMultiAxis(series, orientation);
  }

  //  void QQuickGraphsBars::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall27 call = reinterpret_cast<CuteQQuickGraphsBarsCall27>(taken[27]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleAxisXChanged(axis);
  }

  //  void QQuickGraphsBars::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall28 call = reinterpret_cast<CuteQQuickGraphsBarsCall28>(taken[28]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleAxisYChanged(axis);
  }

  //  void QQuickGraphsBars::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall29 call = reinterpret_cast<CuteQQuickGraphsBarsCall29>(taken[29]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsBars::handleAxisZChanged(axis);
  }

  //  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject
  //      *sender)
  void handleAxisTitleChangedBySender(QObject *sender) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall30 call = reinterpret_cast<CuteQQuickGraphsBarsCall30>(taken[30]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject
  //      *sender)
  void handleAxisLabelsChangedBySender(QObject *sender) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall31 call = reinterpret_cast<CuteQQuickGraphsBarsCall31>(taken[31]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelsChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
  //      *sender)
  void handleAxisSegmentCountChangedBySender(QObject *sender) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall32 call = reinterpret_cast<CuteQQuickGraphsBarsCall32>(taken[32]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSegmentCountChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObjec
  //      t *sender)
  void handleAxisSubSegmentCountChangedBySender(QObject *sender) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall33 call = reinterpret_cast<CuteQQuickGraphsBarsCall33>(taken[33]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
  //      *sender)
  void handleAxisLabelFormatChangedBySender(QObject *sender) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall34 call = reinterpret_cast<CuteQQuickGraphsBarsCall34>(taken[34]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelFormatChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject
  //      *sender)
  void handleAxisReversedChangedBySender(QObject *sender) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall35 call = reinterpret_cast<CuteQQuickGraphsBarsCall35>(taken[35]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisReversedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject
  //      *sender)
  void handleAxisFormatterDirtyBySender(QObject *sender) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall36 call = reinterpret_cast<CuteQQuickGraphsBarsCall36>(taken[36]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisFormatterDirtyBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObj
  //      ect *sender)
  void handleAxisLabelAutoRotationChangedBySender(QObject *sender) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall37 call = reinterpret_cast<CuteQQuickGraphsBarsCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall38 call = reinterpret_cast<CuteQQuickGraphsBarsCall38>(taken[38]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
  //      *sender)
  void handleAxisLabelSizeChangedBySender(QObject *sender) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall39 call = reinterpret_cast<CuteQQuickGraphsBarsCall39>(taken[39]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelSizeChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisTitleVisibilityChangedBySender(QObject *sender) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall40 call = reinterpret_cast<CuteQQuickGraphsBarsCall40>(taken[40]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisLabelVisibilityChangedBySender(QObject *sender) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall41 call = reinterpret_cast<CuteQQuickGraphsBarsCall41>(taken[41]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
  //      *sender)
  void handleAxisTitleFixedChangedBySender(QObject *sender) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall42 call = reinterpret_cast<CuteQQuickGraphsBarsCall42>(taken[42]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleFixedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
  //      *sender)
  void handleAxisTitleOffsetChangedBySender(QObject *sender) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall43 call = reinterpret_cast<CuteQQuickGraphsBarsCall43>(taken[43]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(sender);
  }

  //  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall44 call = reinterpret_cast<CuteQQuickGraphsBarsCall44>(taken[44]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addSeriesInternal(series);
  }

  //  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries
  //      *series)
  void removeSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall45 call = reinterpret_cast<CuteQQuickGraphsBarsCall45>(taken[45]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeSeriesInternal(series);
  }

  //  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
  void addAxis(QAbstract3DAxis *axis) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall46 call = reinterpret_cast<CuteQQuickGraphsBarsCall46>(taken[46]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addAxis(axis);
  }

  //  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
  void releaseAxis(QAbstract3DAxis *axis) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall47 call = reinterpret_cast<CuteQQuickGraphsBarsCall47>(taken[47]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseAxis(axis);
  }

  //  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode
  //      mode)
  void setRenderingMode(QtGraphs3D::RenderingMode mode) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall48 call = reinterpret_cast<CuteQQuickGraphsBarsCall48>(taken[48]);
      call(this, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setRenderingMode(mode);
  }

  //  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
  QtGraphs3D::RenderingMode renderingMode() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall49 call = reinterpret_cast<CuteQQuickGraphsBarsCall49>(taken[49]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::RenderingMode>(given);
    }
    return QQuickGraphsItem::renderingMode();
  }

  //  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::Transpare
  //      ncyTechnique technique)
  void setTransparencyTechnique(
      QtGraphs3D::TransparencyTechnique technique) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall50 call = reinterpret_cast<CuteQQuickGraphsBarsCall50>(taken[50]);
      call(this, static_cast<int>(technique), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setTransparencyTechnique(technique);
  }

  //  QtGraphs3D::TransparencyTechnique
  //      QQuickGraphsItem::transparencyTechnique() const
  QtGraphs3D::TransparencyTechnique transparencyTechnique() const override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall51 call = reinterpret_cast<CuteQQuickGraphsBarsCall51>(taken[51]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::TransparencyTechnique>(given);
    }
    return QQuickGraphsItem::transparencyTechnique();
  }

  //  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
  QtGraphs3D::SelectionFlags selectionMode() const override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall52 call = reinterpret_cast<CuteQQuickGraphsBarsCall52>(taken[52]);
      int given = call(this, &handled);
      if (handled) return QFlags<QtGraphs3D::SelectionFlag>::fromInt(given);
    }
    return QQuickGraphsItem::selectionMode();
  }

  //  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void setShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall53 call = reinterpret_cast<CuteQQuickGraphsBarsCall53>(taken[53]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setShadowQuality(quality);
  }

  //  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
  QtGraphs3D::ShadowQuality shadowQuality() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall54 call = reinterpret_cast<CuteQQuickGraphsBarsCall54>(taken[54]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ShadowQuality>(given);
    }
    return QQuickGraphsItem::shadowQuality();
  }

  //  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
  QtGraphs3D::ElementType selectedElement() const override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall55 call = reinterpret_cast<CuteQQuickGraphsBarsCall55>(taken[55]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ElementType>(given);
    }
    return QQuickGraphsItem::selectedElement();
  }

  //  void QQuickGraphsItem::setMsaaSamples(int samples)
  void setMsaaSamples(int samples) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall56 call = reinterpret_cast<CuteQQuickGraphsBarsCall56>(taken[56]);
      call(this, samples, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setMsaaSamples(samples);
  }

  //  int QQuickGraphsItem::msaaSamples() const
  int msaaSamples() const override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall57 call = reinterpret_cast<CuteQQuickGraphsBarsCall57>(taken[57]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::msaaSamples();
  }

  //  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall58 call = reinterpret_cast<CuteQQuickGraphsBarsCall58>(taken[58]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::hasSeries(series);
  }

  //  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall59 call = reinterpret_cast<CuteQQuickGraphsBarsCall59>(taken[59]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::addCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItems()
  void removeCustomItems() override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall60 call = reinterpret_cast<CuteQQuickGraphsBarsCall60>(taken[60]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItems();
  }

  //  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall61 call = reinterpret_cast<CuteQQuickGraphsBarsCall61>(taken[61]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall62 call = reinterpret_cast<CuteQQuickGraphsBarsCall62>(taken[62]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItemAt(position);
  }

  //  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall63 call = reinterpret_cast<CuteQQuickGraphsBarsCall63>(taken[63]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseCustomItem(item);
  }

  //  int QQuickGraphsItem::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall64 call = reinterpret_cast<CuteQQuickGraphsBarsCall64>(taken[64]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall65 call = reinterpret_cast<CuteQQuickGraphsBarsCall65>(taken[65]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::selectedAxis();
  }

  //  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall66 call = reinterpret_cast<CuteQQuickGraphsBarsCall66>(taken[66]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall67 call = reinterpret_cast<CuteQQuickGraphsBarsCall67>(taken[67]);
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
    if (taken[68]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall68 call = reinterpret_cast<CuteQQuickGraphsBarsCall68>(taken[68]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickGraphsItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall69 call = reinterpret_cast<CuteQQuickGraphsBarsCall69>(taken[69]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickGraphsItem::handleWindowChanged()
  void handleWindowChanged() override {
    if (taken[70]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall70 call = reinterpret_cast<CuteQQuickGraphsBarsCall70>(taken[70]);
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
    if (taken[71]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall71 call = reinterpret_cast<CuteQQuickGraphsBarsCall71>(taken[71]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::itemChange(change, value);
  }

  //  void QQuickGraphsItem::updateWindowParameters()
  void updateWindowParameters() override {
    if (taken[72]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall72 call = reinterpret_cast<CuteQQuickGraphsBarsCall72>(taken[72]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateWindowParameters();
  }

  //  void QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::Selectio
  //      nFlags mode)
  void handleSelectionModeChange(QtGraphs3D::SelectionFlags mode) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall73 call = reinterpret_cast<CuteQQuickGraphsBarsCall73>(taken[73]);
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
    if (taken[74]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall74 call = reinterpret_cast<CuteQQuickGraphsBarsCall74>(taken[74]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleShadowQualityChange(quality);
  }

  //  void
  //      QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::Element
  //      Type type)
  void handleSelectedElementChange(QtGraphs3D::ElementType type) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall75 call = reinterpret_cast<CuteQQuickGraphsBarsCall75>(taken[75]);
      call(this, static_cast<int>(type), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSelectedElementChange(type);
  }

  //  void QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::Optim
  //      izationHint hint)
  void handleOptimizationHintChange(
      QtGraphs3D::OptimizationHint hint) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall76 call = reinterpret_cast<CuteQQuickGraphsBarsCall76>(taken[76]);
      call(this, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleOptimizationHintChange(hint);
  }

  //  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall77 call = reinterpret_cast<CuteQQuickGraphsBarsCall77>(taken[77]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::keyPressEvent(ev);
  }

  //  void QQuickGraphsItem::handleThemeTypeChange()
  void handleThemeTypeChange() override {
    if (taken[78]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall78 call = reinterpret_cast<CuteQQuickGraphsBarsCall78>(taken[78]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleThemeTypeChange();
  }

  //  void QQuickGraphsItem::handleParentWidthChange()
  void handleParentWidthChange() override {
    if (taken[79]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall79 call = reinterpret_cast<CuteQQuickGraphsBarsCall79>(taken[79]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentWidthChange();
  }

  //  void QQuickGraphsItem::handleParentHeightChange()
  void handleParentHeightChange() override {
    if (taken[80]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall80 call = reinterpret_cast<CuteQQuickGraphsBarsCall80>(taken[80]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentHeightChange();
  }

  //  void QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void updateShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall81 call = reinterpret_cast<CuteQQuickGraphsBarsCall81>(taken[81]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateShadowQuality(quality);
  }

  //  void QQuickGraphsItem::updateSingleHighlightColor()
  void updateSingleHighlightColor() override {
    if (taken[82]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall82 call = reinterpret_cast<CuteQQuickGraphsBarsCall82>(taken[82]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSingleHighlightColor();
  }

  //  void QQuickGraphsItem::startRecordingRemovesAndInserts()
  void startRecordingRemovesAndInserts() override {
    if (taken[83]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall83 call = reinterpret_cast<CuteQQuickGraphsBarsCall83>(taken[83]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::startRecordingRemovesAndInserts();
  }

  //  bool QQuick3DViewport::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[84]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall84 call = reinterpret_cast<CuteQQuickGraphsBarsCall84>(taken[84]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DViewport::isTextureProvider();
  }

  //  QSGTextureProvider *QQuick3DViewport::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[85]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall85 call = reinterpret_cast<CuteQQuickGraphsBarsCall85>(taken[85]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuick3DViewport::textureProvider();
  }

  //  void QQuick3DViewport::releaseResources()
  void releaseResources() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall86 call = reinterpret_cast<CuteQQuickGraphsBarsCall86>(taken[86]);
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
      CuteQQuickGraphsBarsCall87 call = reinterpret_cast<CuteQQuickGraphsBarsCall87>(taken[87]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuick3DViewport::updatePaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[88]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall88 call = reinterpret_cast<CuteQQuickGraphsBarsCall88>(taken[88]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[89]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall89 call = reinterpret_cast<CuteQQuickGraphsBarsCall89>(taken[89]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[90]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall90 call = reinterpret_cast<CuteQQuickGraphsBarsCall90>(taken[90]);
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
      CuteQQuickGraphsBarsCall91 call = reinterpret_cast<CuteQQuickGraphsBarsCall91>(taken[91]);
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
      CuteQQuickGraphsBarsCall92 call = reinterpret_cast<CuteQQuickGraphsBarsCall92>(taken[92]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall93 call = reinterpret_cast<CuteQQuickGraphsBarsCall93>(taken[93]);
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
      CuteQQuickGraphsBarsCall94 call = reinterpret_cast<CuteQQuickGraphsBarsCall94>(taken[94]);
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
      CuteQQuickGraphsBarsCall95 call = reinterpret_cast<CuteQQuickGraphsBarsCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall96 call = reinterpret_cast<CuteQQuickGraphsBarsCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall97 call = reinterpret_cast<CuteQQuickGraphsBarsCall97>(taken[97]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall98 call = reinterpret_cast<CuteQQuickGraphsBarsCall98>(taken[98]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall99 call = reinterpret_cast<CuteQQuickGraphsBarsCall99>(taken[99]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall100 call = reinterpret_cast<CuteQQuickGraphsBarsCall100>(taken[100]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall101 call = reinterpret_cast<CuteQQuickGraphsBarsCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[102]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall102 call = reinterpret_cast<CuteQQuickGraphsBarsCall102>(taken[102]);
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
      CuteQQuickGraphsBarsCall103 call = reinterpret_cast<CuteQQuickGraphsBarsCall103>(taken[103]);
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
      CuteQQuickGraphsBarsCall104 call = reinterpret_cast<CuteQQuickGraphsBarsCall104>(taken[104]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall105 call = reinterpret_cast<CuteQQuickGraphsBarsCall105>(taken[105]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall106 call = reinterpret_cast<CuteQQuickGraphsBarsCall106>(taken[106]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall107 call = reinterpret_cast<CuteQQuickGraphsBarsCall107>(taken[107]);
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
      CuteQQuickGraphsBarsCall108 call = reinterpret_cast<CuteQQuickGraphsBarsCall108>(taken[108]);
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
      CuteQQuickGraphsBarsCall109 call = reinterpret_cast<CuteQQuickGraphsBarsCall109>(taken[109]);
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
      CuteQQuickGraphsBarsCall110 call = reinterpret_cast<CuteQQuickGraphsBarsCall110>(taken[110]);
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
      CuteQQuickGraphsBarsCall111 call = reinterpret_cast<CuteQQuickGraphsBarsCall111>(taken[111]);
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
      CuteQQuickGraphsBarsCall112 call = reinterpret_cast<CuteQQuickGraphsBarsCall112>(taken[112]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[113]) {
      int handled = 0;
      CuteQQuickGraphsBarsCall113 call = reinterpret_cast<CuteQQuickGraphsBarsCall113>(taken[113]);
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
      CuteQQuickGraphsBarsCall114 call = reinterpret_cast<CuteQQuickGraphsBarsCall114>(taken[114]);
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
      CuteQQuickGraphsBarsCall115 call = reinterpret_cast<CuteQQuickGraphsBarsCall115>(taken[115]);
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
      CuteQQuickGraphsBarsCall116 call = reinterpret_cast<CuteQQuickGraphsBarsCall116>(taken[116]);
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
      CuteQQuickGraphsBarsCall117 call = reinterpret_cast<CuteQQuickGraphsBarsCall117>(taken[117]);
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
      CuteQQuickGraphsBarsCall118 call = reinterpret_cast<CuteQQuickGraphsBarsCall118>(taken[118]);
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
      CuteQQuickGraphsBarsCall119 call = reinterpret_cast<CuteQQuickGraphsBarsCall119>(taken[119]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsBars::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickGraphsBars10metaObjectEv(
    const QQuickGraphsBars *self) {
  return self->metaObject();
}

//  QString QQuickGraphsBars::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickGraphsBars2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsBars::tr(s, c, n));
}

//  QQuickGraphsBars::QQuickGraphsBars(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsBars *ritual_ZN16QQuickGraphsBarsC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickGraphsBars(parent);
}

//  QQuickGraphsBars::~QQuickGraphsBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBarsD1Ev(QQuickGraphsBars *self) {
  delete self;
}

//  QCategory3DAxis *QQuickGraphsBars::rowAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK16QQuickGraphsBars7rowAxisEv(
    const QQuickGraphsBars *self) {
  return self->rowAxis();
}

//  void QQuickGraphsBars::setRowAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars10setRowAxisEP15QCategory3DAxis(
    QQuickGraphsBars *self,
    QCategory3DAxis *axis) {
  self->setRowAxis(axis);
}

//  QValue3DAxis *QQuickGraphsBars::valueAxis() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK16QQuickGraphsBars9valueAxisEv(
    const QQuickGraphsBars *self) {
  return self->valueAxis();
}

//  void QQuickGraphsBars::setValueAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars12setValueAxisEP12QValue3DAxis(
    QQuickGraphsBars *self,
    QValue3DAxis *axis) {
  self->setValueAxis(axis);
}

//  QCategory3DAxis *QQuickGraphsBars::columnAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK16QQuickGraphsBars10columnAxisEv(
    const QQuickGraphsBars *self) {
  return self->columnAxis();
}

//  void QQuickGraphsBars::setColumnAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars13setColumnAxisEP15QCategory3DAxis(
    QQuickGraphsBars *self,
    QCategory3DAxis *axis) {
  self->setColumnAxis(axis);
}

//  void QQuickGraphsBars::setMultiSeriesUniform(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars21setMultiSeriesUniformEb(
    QQuickGraphsBars *self,
    bool uniform) {
  self->setMultiSeriesUniform(uniform);
}

//  bool QQuickGraphsBars::isMultiSeriesUniform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsBars20isMultiSeriesUniformEv(
    const QQuickGraphsBars *self) {
  return self->isMultiSeriesUniform();
}

//  void QQuickGraphsBars::setBarThickness(float thicknessRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars15setBarThicknessEf(
    QQuickGraphsBars *self,
    float thicknessRatio) {
  self->setBarThickness(thicknessRatio);
}

//  float QQuickGraphsBars::barThickness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsBars12barThicknessEv(
    const QQuickGraphsBars *self) {
  return self->barThickness();
}

//  void QQuickGraphsBars::setBarSpacing(QSizeF spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars13setBarSpacingE6QSizeF(
    QQuickGraphsBars *self,
    const QSizeF *spacing) {
  self->setBarSpacing(*spacing);
}

//  QSizeF QQuickGraphsBars::barSpacing() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK16QQuickGraphsBars10barSpacingEv(
    const QQuickGraphsBars *self) {
  return new QSizeF(self->barSpacing());
}

//  void QQuickGraphsBars::setBarSpacingRelative(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars21setBarSpacingRelativeEb(
    QQuickGraphsBars *self,
    bool relative) {
  self->setBarSpacingRelative(relative);
}

//  bool QQuickGraphsBars::isBarSpacingRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsBars20isBarSpacingRelativeEv(
    const QQuickGraphsBars *self) {
  return self->isBarSpacingRelative();
}

//  void QQuickGraphsBars::setBarSeriesMargin(QSizeF margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18setBarSeriesMarginE6QSizeF(
    QQuickGraphsBars *self,
    const QSizeF *margin) {
  self->setBarSeriesMargin(*margin);
}

//  QSizeF QQuickGraphsBars::barSeriesMargin() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK16QQuickGraphsBars15barSeriesMarginEv(
    const QQuickGraphsBars *self) {
  return new QSizeF(self->barSeriesMargin());
}

//  void QQuickGraphsBars::setMultiSeriesScaling(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars21setMultiSeriesScalingEb(
    QQuickGraphsBars *self,
    bool uniform) {
  self->setMultiSeriesScaling(uniform);
}

//  bool QQuickGraphsBars::multiSeriesScaling() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsBars18multiSeriesScalingEv(
    const QQuickGraphsBars *self) {
  return self->multiSeriesScaling();
}

//  void QQuickGraphsBars::setBarSpecs(float thicknessRatio, QSizeF spacing,
//      bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars11setBarSpecsEf6QSizeFb(
    QQuickGraphsBars *self,
    float thicknessRatio,
    const QSizeF *spacing,
    bool relative) {
  self->setBarSpecs(thicknessRatio, *spacing, relative);
}

//  void QQuickGraphsBars::setFloorLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars13setFloorLevelEf(
    QQuickGraphsBars *self,
    float level) {
  self->setFloorLevel(level);
}

//  float QQuickGraphsBars::floorLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsBars10floorLevelEv(
    const QQuickGraphsBars *self) {
  return self->floorLevel();
}

//  void QQuickGraphsBars::addSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars9addSeriesEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->addSeries(series);
}

//  void QQuickGraphsBars::removeSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars12removeSeriesEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->removeSeries(series);
}

//  void QQuickGraphsBars::insertSeries(qsizetype index, QBar3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars12insertSeriesExP12QBar3DSeries(
    QQuickGraphsBars *self,
    qsizetype index,
    QBar3DSeries *series) {
  self->insertSeries(index, series);
}

//  void QQuickGraphsBars::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars14clearSelectionEv(QQuickGraphsBars *self) {
  self->clearSelection();
}

//  void QQuickGraphsBars::setPrimarySeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16setPrimarySeriesEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->setPrimarySeries(series);
}

//  QBar3DSeries *QQuickGraphsBars::primarySeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK16QQuickGraphsBars13primarySeriesEv(
    const QQuickGraphsBars *self) {
  return self->primarySeries();
}

//  QBar3DSeries *QQuickGraphsBars::selectedSeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK16QQuickGraphsBars14selectedSeriesEv(
    const QQuickGraphsBars *self) {
  return self->selectedSeries();
}

//  QPoint QQuickGraphsBars::invalidSelectionPosition()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN16QQuickGraphsBars24invalidSelectionPositionEv() {
  return new QPoint(QQuickGraphsBars::invalidSelectionPosition());
}

//  void QQuickGraphsBars::setSelectionMode(QtGraphs3D::SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsBars *self,
    int mode) {
  self->setSelectionMode(QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(QAbs
//      tract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsBars *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsBars::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsBars *self,
    QObject *sender) {
  self->handleSeriesVisibilityChangedBySender(sender);
}

//  void QQuickGraphsBars::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsBars *self,
    bool visible,
    QObject *sender) {
  self->handleItemLabelVisibleChangedBySender(visible, sender);
}

//  void QQuickGraphsBars::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsBars *self,
    QObject *sender) {
  self->handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsBars::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16adjustAxisRangesEv(
    QQuickGraphsBars *self) {
  self->adjustAxisRanges();
}

//  void QQuickGraphsBars::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars25handleLightingModeChangedEv(
    QQuickGraphsBars *self) {
  self->handleLightingModeChanged();
}

//  void QQuickGraphsBars::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->handleMultiAxisChanged(axis);
}

//  void QQuickGraphsBars::setSelectedBar(QPoint coord, QBar3DSeries *series,
//      bool enterSlice)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars14setSelectedBarE6QPointP12QBar3DSeriesb(
    QQuickGraphsBars *self,
    const QPoint *coord,
    QBar3DSeries *series,
    bool enterSlice) {
  self->setSelectedBar(*coord, series, enterSlice);
}

//  QList<QBar3DSeries *> QQuickGraphsBars::barSeriesList()
extern "C" Q_DECL_EXPORT
QList<QBar3DSeries *> *ritual_ZN16QQuickGraphsBars13barSeriesListEv(
    QQuickGraphsBars *self) {
  return new QList<QBar3DSeries *>(self->barSeriesList());
}

//  bool QQuickGraphsBars::isSeriesVisualsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsBars20isSeriesVisualsDirtyEv(
    const QQuickGraphsBars *self) {
  return self->isSeriesVisualsDirty();
}

//  void QQuickGraphsBars::setSeriesVisualsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars21setSeriesVisualsDirtyEb(
    QQuickGraphsBars *self,
    bool dirty) {
  self->setSeriesVisualsDirty(dirty);
}

//  bool QQuickGraphsBars::isDataDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsBars11isDataDirtyEv(
    const QQuickGraphsBars *self) {
  return self->isDataDirty();
}

//  void QQuickGraphsBars::setDataDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars12setDataDirtyEb(
    QQuickGraphsBars *self,
    bool dirty) {
  self->setDataDirty(dirty);
}

//  void QQuickGraphsBars::renderSliceToImage(int requestedIndex,
//      QtGraphs3D::SliceCaptureType sliceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18renderSliceToImageEiN10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsBars *self,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType) {
  self->renderSliceToImage(requestedIndex, sliceType);
}

//  void QQuickGraphsBars::renderSliceToImage(int requestedIndex,
//      QtGraphs3D::SliceCaptureType sliceType, const QUrl &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18renderSliceToImageEiN10QtGraphs3D16SliceCaptureTypeERK4QUrl(
    QQuickGraphsBars *self,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType,
    const QUrl *filePath) {
  self->renderSliceToImage(requestedIndex, sliceType, *filePath);
}

//  void QQuickGraphsBars::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars17componentCompleteEv(
    QQuickGraphsBars *self) {
  self->componentComplete();
}

//  void QQuickGraphsBars::synchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars9synchDataEv(QQuickGraphsBars *self) {
  self->synchData();
}

//  void QQuickGraphsBars::updateFloor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars11updateFloorEv(QQuickGraphsBars *self) {
  self->updateFloor();
}

//  void QQuickGraphsBars::updateParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16updateParametersEv(
    QQuickGraphsBars *self) {
  self->updateParameters();
}

//  void QQuickGraphsBars::updateFloorLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16updateFloorLevelEf(
    QQuickGraphsBars *self,
    float level) {
  self->updateFloorLevel(level);
}

//  void QQuickGraphsBars::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars11updateGraphEv(QQuickGraphsBars *self) {
  self->updateGraph();
}

//  void QQuickGraphsBars::updateAxisRange(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars15updateAxisRangeEff(
    QQuickGraphsBars *self,
    float min,
    float max) {
  self->updateAxisRange(min, max);
}

//  void QQuickGraphsBars::updateAxisReversed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18updateAxisReversedEb(
    QQuickGraphsBars *self,
    bool enable) {
  self->updateAxisReversed(enable);
}

//  void QQuickGraphsBars::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars19updateLightStrengthEv(
    QQuickGraphsBars *self) {
  self->updateLightStrength();
}

//  void QQuickGraphsBars::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars28calculateSceneScalingFactorsEv(
    QQuickGraphsBars *self) {
  self->calculateSceneScalingFactors();
}

//  QVector3D
//      QQuickGraphsBars::calculateCategoryLabelPosition(QAbstract3DAxis
//      *axis, QVector3D labelPosition, int index)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN16QQuickGraphsBars30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis,
    const QVector3D *labelPosition,
    int index) {
  return new QVector3D(
      self->calculateCategoryLabelPosition(
          axis,
          *labelPosition,
          index));
}

//  float QQuickGraphsBars::calculateCategoryGridLinePosition(QAbstract3DAxis
//      *axis, int index)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QQuickGraphsBars33calculateCategoryGridLinePositionEP15QAbstract3DAxisi(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis,
    int index) {
  return self->calculateCategoryGridLinePosition(axis, index);
}

//  void QQuickGraphsBars::createSliceView()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars15createSliceViewEv(QQuickGraphsBars *self) {
  self->createSliceView();
}

//  void QQuickGraphsBars::toggleSliceGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16toggleSliceGraphEv(
    QQuickGraphsBars *self) {
  self->toggleSliceGraph();
}

//  void QQuickGraphsBars::handleLabelCountChanged(QQuick3DRepeater
//      *repeater, QColor axisLabelColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars23handleLabelCountChangedEP16QQuick3DRepeater6QColor(
    QQuickGraphsBars *self,
    QQuick3DRepeater *repeater,
    const QColor *axisLabelColor) {
  self->handleLabelCountChanged(repeater, *axisLabelColor);
}

//  void QQuickGraphsBars::updateSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsBars *self,
    int mode) {
  self->updateSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  bool QQuickGraphsBars::doPicking(QPointF position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsBars9doPickingE7QPointF(
    QQuickGraphsBars *self,
    const QPointF *position) {
  return self->doPicking(*position);
}

//  bool QQuickGraphsBars::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsBars12doRayPickingE9QVector3DS0_(
    QQuickGraphsBars *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  QAbstract3DAxis
//      *QQuickGraphsBars::createDefaultAxis(QAbstract3DAxis::AxisOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN16QQuickGraphsBars17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsBars *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  void QQuickGraphsBars::updateSliceItemLabel(const QString &label,
//      QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars20updateSliceItemLabelERK7QString9QVector3D(
    QQuickGraphsBars *self,
    const QString *label,
    const QVector3D *position) {
  self->updateSliceItemLabel(*label, *position);
}

//  QAbstract3DAxis *QQuickGraphsBars::getSeriesMultiAxis(QAbstract3DSeries
//      *series, QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN16QQuickGraphsBars18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsBars *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->getSeriesMultiAxis(series, orientation);
}

//  QQuick3DViewport *QQuickGraphsBars::createOffscreenSliceView(int
//      requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN16QQuickGraphsBars24createOffscreenSliceViewEiN10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsBars *self,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType) {
  return self->createOffscreenSliceView(requestedIndex, sliceType);
}

//  void QQuickGraphsBars::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void QQuickGraphsBars::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void QQuickGraphsBars::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  void QQuickGraphsBars::handleSeriesMeshChanged(QAbstract3DSeries::Mesh
//      mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars23handleSeriesMeshChangedEN17QAbstract3DSeries4MeshE(
    QQuickGraphsBars *self,
    QAbstract3DSeries::Mesh mesh) {
  self->handleSeriesMeshChanged(mesh);
}

//  void QQuickGraphsBars::handleMeshSmoothChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars23handleMeshSmoothChangedEb(
    QQuickGraphsBars *self,
    bool enable) {
  self->handleMeshSmoothChanged(enable);
}

//  void QQuickGraphsBars::handleCameraRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars27handleCameraRotationChangedEv(
    QQuickGraphsBars *self) {
  self->handleCameraRotationChanged();
}

//  void QQuickGraphsBars::handleArrayReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16handleArrayResetEv(
    QQuickGraphsBars *self) {
  self->handleArrayReset();
}

//  void QQuickGraphsBars::handleRowsAdded(qsizetype startIndex, qsizetype
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars15handleRowsAddedExx(
    QQuickGraphsBars *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsAdded(startIndex, count);
}

//  void QQuickGraphsBars::handleRowsChanged(qsizetype startIndex, qsizetype
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars17handleRowsChangedExx(
    QQuickGraphsBars *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsChanged(startIndex, count);
}

//  void QQuickGraphsBars::handleRowsRemoved(qsizetype startIndex, qsizetype
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars17handleRowsRemovedExx(
    QQuickGraphsBars *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsRemoved(startIndex, count);
}

//  void QQuickGraphsBars::handleRowsInserted(qsizetype startIndex, qsizetype
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18handleRowsInsertedExx(
    QQuickGraphsBars *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsInserted(startIndex, count);
}

//  void QQuickGraphsBars::handleItemChanged(qsizetype rowIndex, qsizetype
//      columnIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars17handleItemChangedExx(
    QQuickGraphsBars *self,
    qsizetype rowIndex,
    qsizetype columnIndex) {
  self->handleItemChanged(rowIndex, columnIndex);
}

//  void QQuickGraphsBars::handleDataRowLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars26handleDataRowLabelsChangedEv(
    QQuickGraphsBars *self) {
  self->handleDataRowLabelsChanged();
}

//  void QQuickGraphsBars::handleDataColumnLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars29handleDataColumnLabelsChangedEv(
    QQuickGraphsBars *self) {
  self->handleDataColumnLabelsChanged();
}

//  void QQuickGraphsBars::handleRowColorsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars22handleRowColorsChangedEv(
    QQuickGraphsBars *self) {
  self->handleRowColorsChanged();
}

//  void QQuickGraphsBars::handleValueColoringChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars26handleValueColoringChangedEv(
    QQuickGraphsBars *self) {
  self->handleValueColoringChanged();
}

//  void QQuickGraphsBars::calculateHeightAdjustment()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars25calculateHeightAdjustmentEv(
    QQuickGraphsBars *self) {
  self->calculateHeightAdjustment();
}

//  void QQuickGraphsBars::calculateSeriesStartPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars28calculateSeriesStartPositionEv(
    QQuickGraphsBars *self) {
  self->calculateSeriesStartPosition();
}

//  void QQuickGraphsBars::connectSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars13connectSeriesEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->connectSeries(series);
}

//  void QQuickGraphsBars::disconnectSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16disconnectSeriesEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->disconnectSeries(series);
}

//  QQuick3DModel *QQuickGraphsBars::createDataItem(QQuick3DNode *scene,
//      QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZN16QQuickGraphsBars14createDataItemEP12QQuick3DNodeP17QAbstract3DSeries(
    QQuickGraphsBars *self,
    QQuick3DNode *scene,
    QAbstract3DSeries *series) {
  return self->createDataItem(scene, series);
}

//  QString QQuickGraphsBars::getMeshFileName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickGraphsBars15getMeshFileNameEv(
    QQuickGraphsBars *self) {
  return new QString(self->getMeshFileName());
}

//  void QQuickGraphsBars::updateBarVisuality(QBar3DSeries *series, int
//      visualIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18updateBarVisualityEP12QBar3DSeriesi(
    QQuickGraphsBars *self,
    QBar3DSeries *series,
    int visualIndex) {
  self->updateBarVisuality(series, visualIndex);
}

//  void QQuickGraphsBars::updateBarPositions(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18updateBarPositionsEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->updateBarPositions(series);
}

//  float QQuickGraphsBars::updateBarHeightParameters(const QBarDataItem
//      *item, QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QQuickGraphsBars25updateBarHeightParametersEPK12QBarDataItemP12QValue3DAxis(
    QQuickGraphsBars *self,
    const QBarDataItem *item,
    QValue3DAxis *axis) {
  return self->updateBarHeightParameters(item, axis);
}

//  void QQuickGraphsBars::updateBarVisuals(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars16updateBarVisualsEP12QBar3DSeries(
    QQuickGraphsBars *self,
    QBar3DSeries *series) {
  self->updateBarVisuals(series);
}

//  void QQuickGraphsBars::updateItemMaterial(QQuick3DModel *item, bool
//      useGradient, bool rangeGradient, const QString &materialName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18updateItemMaterialEP13QQuick3DModelbbRK7QString(
    QQuickGraphsBars *self,
    QQuick3DModel *item,
    bool useGradient,
    bool rangeGradient,
    const QString *materialName) {
  self->updateItemMaterial(item, useGradient, rangeGradient, *materialName);
}

//  void QQuickGraphsBars::updateMaterialProperties(QQuick3DModel *item,
//      const bool isHighlight, const bool isMultiHighlight, QQuick3DTexture
//      *texture, QColor color, const bool transparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars24updateMaterialPropertiesEP13QQuick3DModelbbP15QQuick3DTexture6QColorb(
    QQuickGraphsBars *self,
    QQuick3DModel *item,
    bool isHighlight,
    bool isMultiHighlight,
    QQuick3DTexture *texture,
    const QColor *color,
    bool transparency) {
  self->updateMaterialProperties(
      item,
      isHighlight,
      isMultiHighlight,
      texture,
      *color,
      transparency);
}

//  void QQuickGraphsBars::removeBarModels()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars15removeBarModelsEv(QQuickGraphsBars *self) {
  self->removeBarModels();
}

//  void QQuickGraphsBars::deleteBarModels(QQuick3DModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars15deleteBarModelsEP13QQuick3DModel(
    QQuickGraphsBars *self,
    QQuick3DModel *model) {
  self->deleteBarModels(model);
}

//  void QQuickGraphsBars::deleteBarItemHolders(BarInstancing *instancing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars20deleteBarItemHoldersEP13BarInstancing(
    QQuickGraphsBars *self,
    BarInstancing *instancing) {
  self->deleteBarItemHolders(instancing);
}

//  QQuick3DTexture *QQuickGraphsBars::createTexture()
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZN16QQuickGraphsBars13createTextureEv(
    QQuickGraphsBars *self) {
  return self->createTexture();
}

//  void QQuickGraphsBars::updateSelectedBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars17updateSelectedBarEv(
    QQuickGraphsBars *self) {
  self->updateSelectedBar();
}

//  SelectionType QQuickGraphsBars::isSelected(int row, int bar, QBar3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
QQuickGraphsBars::SelectionType ritual_ZN16QQuickGraphsBars10isSelectedEiiP12QBar3DSeries(
    QQuickGraphsBars *self,
    int row,
    int bar,
    QBar3DSeries *series) {
  return self->isSelected(row, bar, series);
}

//  void QQuickGraphsBars::resetClickedStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars18resetClickedStatusEv(
    QQuickGraphsBars *self) {
  self->resetClickedStatus();
}

//  void QQuickGraphsBars::removeSlicedBarModels()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars21removeSlicedBarModelsEv(
    QQuickGraphsBars *self) {
  self->removeSlicedBarModels();
}

//  void QQuickGraphsBars::updateBarSpecs(float thicknessRatio, QSizeF
//      spacing, bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars14updateBarSpecsEf6QSizeFb(
    QQuickGraphsBars *self,
    float thicknessRatio,
    const QSizeF *spacing,
    bool relative) {
  self->updateBarSpecs(thicknessRatio, *spacing, relative);
}

//  void QQuickGraphsBars::updateBarSeriesMargin(QSizeF margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsBars21updateBarSeriesMarginE6QSizeF(
    QQuickGraphsBars *self,
    const QSizeF *margin) {
  self->updateBarSeriesMargin(*margin);
}

//  a Python function taken by a CuteQQuickGraphsBars, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsBars(
    QQuickGraphsBars *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsBars *>(self)->take(key, call);
}

//  void QQuickGraphsBars::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars14clearSelectionEv(
    QQuickGraphsBars *self) {
  self->QQuickGraphsBars::clearSelection();
}

//  void QQuickGraphsBars::setSelectionMode(QtGraphs3D::SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsBars *self,
    int mode) {
  self->QQuickGraphsBars::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(QAbs
//      tract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsBars *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsBars::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsBars *self,
    QObject *sender) {
  self->QQuickGraphsBars::handleSeriesVisibilityChangedBySender(sender);
}

//  void QQuickGraphsBars::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsBars *self,
    bool visible,
    QObject *sender) {
  self->QQuickGraphsBars::handleItemLabelVisibleChangedBySender(
      visible,
      sender);
}

//  void QQuickGraphsBars::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsBars *self,
    QObject *sender) {
  self->QQuickGraphsBars::handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsBars::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars16adjustAxisRangesEv(
    QQuickGraphsBars *self) {
  self->QQuickGraphsBars::adjustAxisRanges();
}

//  void QQuickGraphsBars::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars25handleLightingModeChangedEv(
    QQuickGraphsBars *self) {
  self->QQuickGraphsBars::handleLightingModeChanged();
}

//  void QQuickGraphsBars::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsBars::handleMultiAxisChanged(axis);
}

//  void QQuickGraphsBars::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars17componentCompleteEv(
    QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::componentComplete();
}

//  void QQuickGraphsBars::synchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars9synchDataEv(QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::synchData();
}

//  void QQuickGraphsBars::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars11updateGraphEv(QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::updateGraph();
}

//  void QQuickGraphsBars::updateAxisRange(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars15updateAxisRangeEff(
    QQuickGraphsBars *self,
    float min,
    float max) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::updateAxisRange(
      min,
      max);
}

//  void QQuickGraphsBars::updateAxisReversed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars18updateAxisReversedEb(
    QQuickGraphsBars *self,
    bool enable) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::updateAxisReversed(
      enable);
}

//  void QQuickGraphsBars::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars19updateLightStrengthEv(
    QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::updateLightStrength();
}

//  void QQuickGraphsBars::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars28calculateSceneScalingFactorsEv(
    QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::calculateSceneScalingFactors();
}

//  QVector3D
//      QQuickGraphsBars::calculateCategoryLabelPosition(QAbstract3DAxis
//      *axis, QVector3D labelPosition, int index)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN16QQuickGraphsBars30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis,
    const QVector3D *labelPosition,
    int index) {
  return new QVector3D(
      static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::calculateCategoryLabelPosition(
          axis,
          *labelPosition,
          index));
}

//  float QQuickGraphsBars::calculateCategoryGridLinePosition(QAbstract3DAxis
//      *axis, int index)
extern "C" Q_DECL_EXPORT
float ritual_own_ZN16QQuickGraphsBars33calculateCategoryGridLinePositionEP15QAbstract3DAxisi(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis,
    int index) {
  return static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::calculateCategoryGridLinePosition(
      axis,
      index);
}

//  void QQuickGraphsBars::createSliceView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars15createSliceViewEv(
    QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::createSliceView();
}

//  void QQuickGraphsBars::toggleSliceGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars16toggleSliceGraphEv(
    QQuickGraphsBars *self) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::toggleSliceGraph();
}

//  void QQuickGraphsBars::handleLabelCountChanged(QQuick3DRepeater
//      *repeater, QColor axisLabelColor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars23handleLabelCountChangedEP16QQuick3DRepeater6QColor(
    QQuickGraphsBars *self,
    QQuick3DRepeater *repeater,
    const QColor *axisLabelColor) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::handleLabelCountChanged(
      repeater,
      *axisLabelColor);
}

//  void QQuickGraphsBars::updateSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsBars *self,
    int mode) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::updateSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  bool QQuickGraphsBars::doPicking(QPointF position)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsBars9doPickingE7QPointF(
    QQuickGraphsBars *self,
    const QPointF *position) {
  return static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::doPicking(
      *position);
}

//  bool QQuickGraphsBars::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsBars12doRayPickingE9QVector3DS0_(
    QQuickGraphsBars *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::doRayPicking(
      *origin,
      *direction);
}

//  QAbstract3DAxis
//      *QQuickGraphsBars::createDefaultAxis(QAbstract3DAxis::AxisOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN16QQuickGraphsBars17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsBars *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::createDefaultAxis(
      orientation);
}

//  void QQuickGraphsBars::updateSliceItemLabel(const QString &label,
//      QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars20updateSliceItemLabelERK7QString9QVector3D(
    QQuickGraphsBars *self,
    const QString *label,
    const QVector3D *position) {
  static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::updateSliceItemLabel(
      *label,
      *position);
}

//  QAbstract3DAxis *QQuickGraphsBars::getSeriesMultiAxis(QAbstract3DSeries
//      *series, QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN16QQuickGraphsBars18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsBars *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnQQuickGraphsBars *>(self)->OwnQQuickGraphsBars::getSeriesMultiAxis(
      series,
      orientation);
}

//  void QQuickGraphsBars::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsBars::handleAxisXChanged(axis);
}

//  void QQuickGraphsBars::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsBars::handleAxisYChanged(axis);
}

//  void QQuickGraphsBars::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsBars18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsBars *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsBars::handleAxisZChanged(axis);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
