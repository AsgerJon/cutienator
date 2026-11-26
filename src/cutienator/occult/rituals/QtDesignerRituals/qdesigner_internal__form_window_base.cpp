//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/formwindowbase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/formwindowbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/grid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/abstractdnditem.h>
#include <QtWidgets/qwidget.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/deviceprofile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdir.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A qdesigner_internal::FormWindowBase that Python can take functions over in. Every qdesigner_internal::FormWindowBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPoint * (*Cuteqdesigner_internal_FormWindowBaseCall0)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall1)(const void *, const QPoint *, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall2)(const void *, int, int *);
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall3)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall4)(const void *, int, int *);
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall5)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall6)(const void *, int, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall7)(const void *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall8)(const void *, const QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall9)(const void *, QWidget *, bool, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall10)(const void *, QWidget *, const QPoint *, int, int *);
#if QT_CONFIG(clipboard)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall11)(const void *, int, int *);
#endif  // QT_CONFIG(clipboard)
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall12)(const void *, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall13)(const void *, bool, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall14)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall15)(const void *, QtResourceSet *, int *);
typedef QString * (*Cuteqdesigner_internal_FormWindowBaseCall16)(const void *, int *);
typedef const QDir * (*Cuteqdesigner_internal_FormWindowBaseCall17)(const void *, int *);
typedef QString * (*Cuteqdesigner_internal_FormWindowBaseCall18)(const void *, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall19)(const void *, QIODevice *, QString *, int *);
typedef QString * (*Cuteqdesigner_internal_FormWindowBaseCall20)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall21)(const void *, const QString *, int *);
typedef QString * (*Cuteqdesigner_internal_FormWindowBaseCall22)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall23)(const void *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall24)(const void *, int, int, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall25)(const void *, QString *, QString *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall26)(const void *, const QString *, const QString *, int *);
typedef QString * (*Cuteqdesigner_internal_FormWindowBaseCall27)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall28)(const void *, const QString *, int *);
typedef QString * (*Cuteqdesigner_internal_FormWindowBaseCall29)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall30)(const void *, const QString *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall31)(const void *, int *);
#if !defined(QT_NO_CURSOR)
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall32)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall33)(const void *, int *);
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall34)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall35)(const void *, int, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall36)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall37)(const void *, QDesignerFormWindowToolInterface *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall38)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall39)(const void *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall40)(const void *, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall41)(const void *, QWidget *, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall42)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall43)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall44)(const void *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall45)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall46)(const void *, QList<QWidget *> *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall47)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall48)(const void *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall49)(const void *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall50)(const void *, QObject *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall51)(const void *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall52)(const void *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall53)(const void *, bool, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall54)(const void *, bool, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall55)(const void *, QWidget *, bool, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall56)(const void *, const QString *, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall57)(const void *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall58)(const void *, int *);
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall59)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall60)(const void *, bool, int *);
typedef const QSize * (*Cuteqdesigner_internal_FormWindowBaseCall61)(const void *, int *);
typedef const QSize * (*Cuteqdesigner_internal_FormWindowBaseCall62)(const void *, int *);
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall63)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall64)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall65)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall66)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall67)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall68)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall69)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall70)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall71)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall72)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall73)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall74)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall75)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall76)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall77)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall78)(const void *, QPaintEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall79)(const void *, QMoveEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall80)(const void *, QResizeEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall81)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall82)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall83)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall84)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall85)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall86)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall87)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall88)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall89)(const void *, QShowEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall90)(const void *, QHideEvent *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall91)(const void *, QEvent *, int *);
typedef int (*Cuteqdesigner_internal_FormWindowBaseCall92)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall93)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall94)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_FormWindowBaseCall95)(const void *, int *);
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall96)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*Cuteqdesigner_internal_FormWindowBaseCall97)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall98)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_FormWindowBaseCall99)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall100)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall101)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall102)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall103)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_FormWindowBaseCall104)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_FormWindowBase : public qdesigner_internal::FormWindowBase {
public:
  using qdesigner_internal::FormWindowBase::FormWindowBase;
  void *taken[105] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface4gridEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface7setGridERK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface10hasFeatureE6QFlagsINS_11FeatureFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface8featuresEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setFeaturesE6QFlagsINS_11FeatureFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface20resourceFileSaveModeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface23setResourceFileSaveModeENS_20ResourceFileSaveModeE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14FormWindowBase19initializePopupMenuEP7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14FormWindowBase8widgetAtERK6QPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal14FormWindowBase13findContainerEP7QWidgetb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14FormWindowBase15highlightWidgetEP7QWidgetRK6QPointNS0_13HighlightModeE")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(clipboard)
    if (!std::strcmp(key, "_ZN18qdesigner_internal14FormWindowBase5pasteENS0_9PasteModeE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(clipboard)
    if (!std::strcmp(key, "_ZN18qdesigner_internal14FormWindowBase17createFormBuilderEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14FormWindowBase21blockSelectionChangedEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11resourceSetEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14setResourceSetEP13QtResourceSet")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface8fileNameEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11absoluteDirEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface8contentsEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setContentsEP9QIODeviceP7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface6authorEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface9setAuthorERK7QString")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface7commentEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface10setCommentERK7QString")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface16setLayoutDefaultEii")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14layoutFunctionEP7QStringS1_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface17setLayoutFunctionERK7QStringS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface14pixmapFunctionEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface17setPixmapFunctionERK7QString")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11exportMacroEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14setExportMacroERK7QString")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface4coreEv")) {
      taken[31] = call;
      return true;
    }
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK7QWidget6cursorEv")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface9toolCountEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11currentToolEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14setCurrentToolEi")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface4toolEi")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12registerToolEP32QDesignerFormWindowToolInterface")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface13mainContainerEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface16setMainContainerEP7QWidget")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface13formContainerEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface9isManagedEP7QWidget")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface7isDirtyEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface14commandHistoryEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12beginCommandERK7QString")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface10endCommandEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface17simplifySelectionEP5QListIP7QWidgetE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface20emitSelectionChangedEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface15addResourceFileERK7QString")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface18removeResourceFileERK7QString")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface22ensureUniqueObjectNameEP7QObject")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12manageWidgetEP7QWidget")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14unmanageWidgetEP7QWidget")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface8setDirtyEb")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14clearSelectionEb")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12selectWidgetEP7QWidgetb")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setFileNameERK7QString")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setContentsERK7QString")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11editWidgetsEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[65] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[66] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[70] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[71] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[81] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[82] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[83] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[84] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[85] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[86] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[87] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[88] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[98] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[99] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[100] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[101] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[102] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[103] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[104] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPoint qdesigner_internal::FormWindowBase::grid() const
  QPoint grid() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall0 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall0>(taken[0]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return qdesigner_internal::FormWindowBase::grid();
  }

  //  void qdesigner_internal::FormWindowBase::setGrid(const QPoint &grid)
  void setGrid(const QPoint &grid) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall1 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall1>(taken[1]);
      call(this, &grid, &handled);
      if (handled) return;
    }
    qdesigner_internal::FormWindowBase::setGrid(grid);
  }

  //  bool qdesigner_internal::FormWindowBase::hasFeature(Feature f) const
  bool hasFeature(QDesignerFormWindowInterface::Feature f) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall2 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall2>(taken[2]);
      bool given = call(this, static_cast<int>(f.toInt()), &handled);
      if (handled) return given;
    }
    return qdesigner_internal::FormWindowBase::hasFeature(f);
  }

  //  Feature qdesigner_internal::FormWindowBase::features() const
  QDesignerFormWindowInterface::Feature features() const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall3 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(given);
    }
    return qdesigner_internal::FormWindowBase::features();
  }

  //  void qdesigner_internal::FormWindowBase::setFeatures(Feature f)
  void setFeatures(QDesignerFormWindowInterface::Feature f) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall4 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall4>(taken[4]);
      call(this, static_cast<int>(f.toInt()), &handled);
      if (handled) return;
    }
    qdesigner_internal::FormWindowBase::setFeatures(f);
  }

  //  ResourceFileSaveMode
  //      qdesigner_internal::FormWindowBase::resourceFileSaveMode() const
  QDesignerFormWindowInterface::ResourceFileSaveMode resourceFileSaveMode() const override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall5 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface::ResourceFileSaveMode>(given);
    }
    return qdesigner_internal::FormWindowBase::resourceFileSaveMode();
  }

  //  void qdesigner_internal::FormWindowBase::setResourceFileSaveMode(Reso
  //      urceFileSaveMode behavior)
  void setResourceFileSaveMode(
      QDesignerFormWindowInterface::ResourceFileSaveMode behavior) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall6 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall6>(taken[6]);
      call(this, static_cast<int>(behavior), &handled);
      if (handled) return;
    }
    qdesigner_internal::FormWindowBase::setResourceFileSaveMode(behavior);
  }

  //  QMenu
  //      *qdesigner_internal::FormWindowBase::initializePopupMenu(QWidget
  //      *managedWidget)
  QMenu *initializePopupMenu(QWidget *managedWidget) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall7 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall7>(taken[7]);
      void * given = call(this, managedWidget, &handled);
      if (handled) return static_cast<QMenu *>(given);
    }
    return qdesigner_internal::FormWindowBase::initializePopupMenu(managedWidget);
  }

  //  QWidget *qdesigner_internal::FormWindowBase::widgetAt(const QPoint
  //      &pos)
  QWidget *widgetAt(const QPoint &pos) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall8 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall8>(taken[8]);
      void * given = call(this, &pos, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QWidget *qdesigner_internal::FormWindowBase::findContainer(QWidget
  //      *w, bool excludeLayout) const
  QWidget *findContainer(QWidget *w, bool excludeLayout) const override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall9 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall9>(taken[9]);
      void * given = call(this, w, excludeLayout, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  void qdesigner_internal::FormWindowBase::highlightWidget(QWidget *w,
  //      const QPoint &pos, HighlightMode mode)
  void highlightWidget(
      QWidget *w,
      const QPoint &pos,
      qdesigner_internal::FormWindowBase::HighlightMode mode) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall10 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall10>(taken[10]);
      call(this, w, &pos, static_cast<int>(mode), &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(clipboard)
  //  void qdesigner_internal::FormWindowBase::paste(PasteMode pasteMode)
  void paste(
      qdesigner_internal::FormWindowBase::PasteMode pasteMode) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall11 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall11>(taken[11]);
      call(this, static_cast<int>(pasteMode), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(clipboard)

  //  QEditorFormBuilder
  //      *qdesigner_internal::FormWindowBase::createFormBuilder()
  qdesigner_internal::QEditorFormBuilder *createFormBuilder() override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall12 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<qdesigner_internal::QEditorFormBuilder *>(given);
    }
    return {};
  }

  //  bool qdesigner_internal::FormWindowBase::blockSelectionChanged(bool
  //      blocked)
  bool blockSelectionChanged(bool blocked) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall13 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall13>(taken[13]);
      bool given = call(this, blocked, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QtResourceSet *qdesigner_internal::FormWindowBase::resourceSet()
  //      const
  QtResourceSet *resourceSet() const override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall14 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QtResourceSet *>(given);
    }
    return qdesigner_internal::FormWindowBase::resourceSet();
  }

  //  void qdesigner_internal::FormWindowBase::setResourceSet(QtResourceSet
  //      *resourceSet)
  void setResourceSet(QtResourceSet *resourceSet) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall15 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall15>(taken[15]);
      call(this, resourceSet, &handled);
      if (handled) return;
    }
    qdesigner_internal::FormWindowBase::setResourceSet(resourceSet);
  }

  //  QString QDesignerFormWindowInterface::fileName() const
  QString fileName() const override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall16 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall16>(taken[16]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QDir QDesignerFormWindowInterface::absoluteDir() const
  QDir absoluteDir() const override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall17 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall17>(taken[17]);
      const QDir * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QString QDesignerFormWindowInterface::contents() const
  QString contents() const override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall18 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall18>(taken[18]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::setContents(QIODevice *dev,
  //      QString *errorMessage)
  bool setContents(QIODevice *dev, QString *errorMessage) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall19 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall19>(taken[19]);
      bool given = call(this, dev, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerFormWindowInterface::author() const
  QString author() const override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall20 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall20>(taken[20]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setAuthor(const QString &author)
  void setAuthor(const QString &author) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall21 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall21>(taken[21]);
      call(this, &author, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerFormWindowInterface::comment() const
  QString comment() const override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall22 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall22>(taken[22]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setComment(const QString &comment)
  void setComment(const QString &comment) override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall23 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall23>(taken[23]);
      call(this, &comment, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setLayoutDefault(int margin, int
  //      spacing)
  void setLayoutDefault(int margin, int spacing) override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall24 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall24>(taken[24]);
      call(this, margin, spacing, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::layoutFunction(QString *margin,
  //      QString *spacing)
  void layoutFunction(QString *margin, QString *spacing) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall25 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall25>(taken[25]);
      call(this, margin, spacing, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setLayoutFunction(const QString
  //      &margin, const QString &spacing)
  void setLayoutFunction(
      const QString &margin,
      const QString &spacing) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall26 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall26>(taken[26]);
      call(this, &margin, &spacing, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerFormWindowInterface::pixmapFunction() const
  QString pixmapFunction() const override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall27 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall27>(taken[27]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setPixmapFunction(const QString
  //      &pixmapFunction)
  void setPixmapFunction(const QString &pixmapFunction) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall28 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall28>(taken[28]);
      call(this, &pixmapFunction, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerFormWindowInterface::exportMacro() const
  QString exportMacro() const override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall29 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall29>(taken[29]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setExportMacro(const QString
  //      &exportMacro)
  void setExportMacro(const QString &exportMacro) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall30 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall30>(taken[30]);
      call(this, &exportMacro, &handled);
      if (handled) return;
    }
  }

  //  QDesignerFormEditorInterface *QDesignerFormWindowInterface::core()
  //      const
  QDesignerFormEditorInterface *core() const override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall31 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return QDesignerFormWindowInterface::core();
  }

#if !defined(QT_NO_CURSOR)
  //  QDesignerFormWindowCursorInterface
  //      *QDesignerFormWindowInterface::cursor() const
  QDesignerFormWindowCursorInterface *cursor() const override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall32 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowCursorInterface *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_CURSOR)

  //  int QDesignerFormWindowInterface::toolCount() const
  int toolCount() const override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall33 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerFormWindowInterface::currentTool() const
  int currentTool() const override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall34 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall34>(taken[34]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setCurrentTool(int index)
  void setCurrentTool(int index) override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall35 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall35>(taken[35]);
      call(this, index, &handled);
      if (handled) return;
    }
  }

  //  QDesignerFormWindowToolInterface
  //      *QDesignerFormWindowInterface::tool(int index) const
  QDesignerFormWindowToolInterface *tool(int index) const override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall36 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall36>(taken[36]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QDesignerFormWindowToolInterface *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::registerTool(QDesignerFormWindowTo
  //      olInterface *tool)
  void registerTool(QDesignerFormWindowToolInterface *tool) override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall37 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall37>(taken[37]);
      call(this, tool, &handled);
      if (handled) return;
    }
  }

  //  QWidget *QDesignerFormWindowInterface::mainContainer() const
  QWidget *mainContainer() const override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall38 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setMainContainer(QWidget
  //      *mainContainer)
  void setMainContainer(QWidget *mainContainer) override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall39 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall39>(taken[39]);
      call(this, mainContainer, &handled);
      if (handled) return;
    }
  }

  //  QWidget *QDesignerFormWindowInterface::formContainer() const
  QWidget *formContainer() const override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall40 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::isManaged(QWidget *widget) const
  bool isManaged(QWidget *widget) const override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall41 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall41>(taken[41]);
      bool given = call(this, widget, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::isDirty() const
  bool isDirty() const override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall42 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QUndoStack *QDesignerFormWindowInterface::commandHistory() const
  QUndoStack *commandHistory() const override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall43 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall43>(taken[43]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QUndoStack *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::beginCommand(const QString
  //      &description)
  void beginCommand(const QString &description) override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall44 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall44>(taken[44]);
      call(this, &description, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::endCommand()
  void endCommand() override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall45 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::simplifySelection(QList<QWidget *>
  //      *widgets) const
  void simplifySelection(QList<QWidget *> *widgets) const override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall46 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall46>(taken[46]);
      call(this, widgets, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::emitSelectionChanged()
  void emitSelectionChanged() override {
    if (taken[47]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall47 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::addResourceFile(const QString
  //      &path)
  void addResourceFile(const QString &path) override {
    if (taken[48]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall48 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall48>(taken[48]);
      call(this, &path, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::removeResourceFile(const QString
  //      &path)
  void removeResourceFile(const QString &path) override {
    if (taken[49]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall49 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall49>(taken[49]);
      call(this, &path, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::ensureUniqueObjectName(QObject
  //      *object)
  void ensureUniqueObjectName(QObject *object) override {
    if (taken[50]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall50 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall50>(taken[50]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::manageWidget(QWidget *widget)
  void manageWidget(QWidget *widget) override {
    if (taken[51]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall51 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall51>(taken[51]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::unmanageWidget(QWidget *widget)
  void unmanageWidget(QWidget *widget) override {
    if (taken[52]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall52 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall52>(taken[52]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setDirty(bool dirty)
  void setDirty(bool dirty) override {
    if (taken[53]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall53 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall53>(taken[53]);
      call(this, dirty, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::clearSelection(bool
  //      changePropertyDisplay)
  void clearSelection(bool changePropertyDisplay) override {
    if (taken[54]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall54 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall54>(taken[54]);
      call(this, changePropertyDisplay, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::selectWidget(QWidget *w, bool
  //      select)
  void selectWidget(QWidget *w, bool select) override {
    if (taken[55]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall55 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall55>(taken[55]);
      call(this, w, select, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setFileName(const QString
  //      &fileName)
  void setFileName(const QString &fileName) override {
    if (taken[56]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall56 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall56>(taken[56]);
      call(this, &fileName, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerFormWindowInterface::setContents(const QString
  //      &contents)
  bool setContents(const QString &contents) override {
    if (taken[57]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall57 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall57>(taken[57]);
      bool given = call(this, &contents, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::editWidgets()
  void editWidgets() override {
    if (taken[58]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall58 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall58>(taken[58]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[59]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall59 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall59>(taken[59]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[60]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall60 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall60>(taken[60]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[61]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall61 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall61>(taken[61]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[62]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall62 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall62>(taken[62]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[63]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall63 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall63>(taken[63]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[64]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall64 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall64>(taken[64]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[65]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall65 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall65>(taken[65]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[66]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall66 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall66>(taken[66]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[67]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall67 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall67>(taken[67]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[68]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall68 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall68>(taken[68]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[69]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall69 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall69>(taken[69]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall70 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall71 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall72 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall73 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall74 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall75 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall76 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall77 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall78 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[79]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall79 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[80]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall80 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall80>(taken[80]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[81]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall81 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall81>(taken[81]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[82]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall82 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall82>(taken[82]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[83]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall83 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall83>(taken[83]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall84 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[85]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall85 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall85>(taken[85]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[86]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall86 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall86>(taken[86]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[87]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall87 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall87>(taken[87]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[88]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall88 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall88>(taken[88]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[89]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall89 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall89>(taken[89]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[90]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall90 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall90>(taken[90]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[91]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall91 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall91>(taken[91]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[92]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall92 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall92>(taken[92]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[93]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall93 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall93>(taken[93]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[94]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall94 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall94>(taken[94]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[95]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall95 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall95>(taken[95]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[96]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall96 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[97]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall97 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall97>(taken[97]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[98]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall98 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall98>(taken[98]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[99]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall99 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall99>(taken[99]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[100]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall100 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall100>(taken[100]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[101]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall101 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall101>(taken[101]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[102]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall102 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall102>(taken[102]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[103]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall103 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall103>(taken[103]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[104]) {
      int handled = 0;
      Cuteqdesigner_internal_FormWindowBaseCall104 call = reinterpret_cast<Cuteqdesigner_internal_FormWindowBaseCall104>(taken[104]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::FormWindowBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14FormWindowBase10metaObjectEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::FormWindowBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14FormWindowBase11qt_metacastEPKc(
    qdesigner_internal::FormWindowBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::FormWindowBase::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14FormWindowBase11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::FormWindowBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::FormWindowBase::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14FormWindowBase2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::FormWindowBase::tr(s, c, n));
}

//  qdesigner_internal::FormWindowBase::~FormWindowBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBaseD1Ev(
    qdesigner_internal::FormWindowBase *self) {
  delete self;
}

//  QVariantMap qdesigner_internal::FormWindowBase::formData()
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN18qdesigner_internal14FormWindowBase8formDataEv(
    qdesigner_internal::FormWindowBase *self) {
  return new QMap<QString, QVariant>(self->formData());
}

//  void qdesigner_internal::FormWindowBase::setFormData(const QVariantMap
//      &vm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase11setFormDataERK4QMapI7QString8QVariantE(
    qdesigner_internal::FormWindowBase *self,
    const QMap<QString, QVariant> *vm) {
  self->setFormData(*vm);
}

//  QStringList qdesigner_internal::FormWindowBase::checkContents() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal14FormWindowBase13checkContentsEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new QList<QString>(self->checkContents());
}

//  QPoint qdesigner_internal::FormWindowBase::grid() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18qdesigner_internal14FormWindowBase4gridEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new QPoint(self->grid());
}

//  void qdesigner_internal::FormWindowBase::setGrid(const QPoint &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase7setGridERK6QPoint(
    qdesigner_internal::FormWindowBase *self,
    const QPoint *grid) {
  self->setGrid(*grid);
}

//  bool qdesigner_internal::FormWindowBase::hasFeature(Feature f) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal14FormWindowBase10hasFeatureE6QFlagsIN28QDesignerFormWindowInterface11FeatureFlagEE(
    const qdesigner_internal::FormWindowBase *self,
    int f) {
  return self->hasFeature(
      QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(f));
}

//  Feature qdesigner_internal::FormWindowBase::features() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14FormWindowBase8featuresEv(
    const qdesigner_internal::FormWindowBase *self) {
  return static_cast<int>(self->features().toInt());
}

//  void qdesigner_internal::FormWindowBase::setFeatures(Feature f)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase11setFeaturesE6QFlagsIN28QDesignerFormWindowInterface11FeatureFlagEE(
    qdesigner_internal::FormWindowBase *self,
    int f) {
  self->setFeatures(
      QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(f));
}

//  const Grid &qdesigner_internal::FormWindowBase::designerGrid() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::Grid *ritual_ZNK18qdesigner_internal14FormWindowBase12designerGridEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new qdesigner_internal::Grid(self->designerGrid());
}

//  void qdesigner_internal::FormWindowBase::setDesignerGrid(const Grid
//      &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase15setDesignerGridERKNS_4GridE(
    qdesigner_internal::FormWindowBase *self,
    const qdesigner_internal::Grid *grid) {
  self->setDesignerGrid(*grid);
}

//  bool qdesigner_internal::FormWindowBase::hasFormGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal14FormWindowBase11hasFormGridEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->hasFormGrid();
}

//  void qdesigner_internal::FormWindowBase::setHasFormGrid(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase14setHasFormGridEb(
    qdesigner_internal::FormWindowBase *self,
    bool b) {
  self->setHasFormGrid(b);
}

//  bool qdesigner_internal::FormWindowBase::gridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal14FormWindowBase11gridVisibleEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->gridVisible();
}

//  ResourceFileSaveMode
//      qdesigner_internal::FormWindowBase::resourceFileSaveMode() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface::ResourceFileSaveMode ritual_ZNK18qdesigner_internal14FormWindowBase20resourceFileSaveModeEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->resourceFileSaveMode();
}

//  void qdesigner_internal::FormWindowBase::setResourceFileSaveMode(Resource
//      FileSaveMode behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase23setResourceFileSaveModeEN28QDesignerFormWindowInterface20ResourceFileSaveModeE(
    qdesigner_internal::FormWindowBase *self,
    QDesignerFormWindowInterface::ResourceFileSaveMode behavior) {
  self->setResourceFileSaveMode(behavior);
}

//  const Grid &qdesigner_internal::FormWindowBase::defaultDesignerGrid()
extern "C" Q_DECL_EXPORT
qdesigner_internal::Grid *ritual_ZN18qdesigner_internal14FormWindowBase19defaultDesignerGridEv() {
  return new qdesigner_internal::Grid(
      qdesigner_internal::FormWindowBase::defaultDesignerGrid());
}

//  void qdesigner_internal::FormWindowBase::setDefaultDesignerGrid(const
//      Grid &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase22setDefaultDesignerGridERKNS_4GridE(
    const qdesigner_internal::Grid *grid) {
  qdesigner_internal::FormWindowBase::setDefaultDesignerGrid(*grid);
}

//  QMenu *qdesigner_internal::FormWindowBase::initializePopupMenu(QWidget
//      *managedWidget)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN18qdesigner_internal14FormWindowBase19initializePopupMenuEP7QWidget(
    qdesigner_internal::FormWindowBase *self,
    QWidget *managedWidget) {
  return self->initializePopupMenu(managedWidget);
}

//  QMenu *qdesigner_internal::FormWindowBase::createExtensionTaskMenu(QDesig
//      nerFormWindowInterface *fw, QObject *o, bool trailingSeparator)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN18qdesigner_internal14FormWindowBase23createExtensionTaskMenuEP28QDesignerFormWindowInterfaceP7QObjectb(
    QDesignerFormWindowInterface *fw,
    QObject *o,
    bool trailingSeparator) {
  return qdesigner_internal::FormWindowBase::createExtensionTaskMenu(
      fw,
      o,
      trailingSeparator);
}

//  bool qdesigner_internal::FormWindowBase::dropWidgets(const
//      QList<QDesignerDnDItemInterface *> &item_list, QWidget *target, const
//      QPoint &global_mouse_pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14FormWindowBase11dropWidgetsERK5QListIP25QDesignerDnDItemInterfaceEP7QWidgetRK6QPoint(
    qdesigner_internal::FormWindowBase *self,
    const QList<QDesignerDnDItemInterface *> *item_list,
    QWidget *target,
    const QPoint *global_mouse_pos) {
  return self->dropWidgets(*item_list, target, *global_mouse_pos);
}

//  QWidget *qdesigner_internal::FormWindowBase::widgetUnderMouse(const
//      QPoint &formPos, WidgetUnderMouseMode m)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal14FormWindowBase16widgetUnderMouseERK6QPointNS0_20WidgetUnderMouseModeE(
    qdesigner_internal::FormWindowBase *self,
    const QPoint *formPos,
    qdesigner_internal::FormWindowBase::WidgetUnderMouseMode m) {
  return self->widgetUnderMouse(*formPos, m);
}

//  QWidget *qdesigner_internal::FormWindowBase::widgetAt(const QPoint &pos)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal14FormWindowBase8widgetAtERK6QPoint(
    qdesigner_internal::FormWindowBase *self,
    const QPoint *pos) {
  return self->widgetAt(*pos);
}

//  QWidget *qdesigner_internal::FormWindowBase::findContainer(QWidget *w,
//      bool excludeLayout) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal14FormWindowBase13findContainerEP7QWidgetb(
    const qdesigner_internal::FormWindowBase *self,
    QWidget *w,
    bool excludeLayout) {
  return self->findContainer(w, excludeLayout);
}

//  void qdesigner_internal::FormWindowBase::deleteWidgetList(const
//      QWidgetList &widget_list)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase16deleteWidgetListERK5QListIP7QWidgetE(
    qdesigner_internal::FormWindowBase *self,
    const QList<QWidget *> *widget_list) {
  self->deleteWidgetList(*widget_list);
}

//  void qdesigner_internal::FormWindowBase::highlightWidget(QWidget *w,
//      const QPoint &pos, HighlightMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase15highlightWidgetEP7QWidgetRK6QPointNS0_13HighlightModeE(
    qdesigner_internal::FormWindowBase *self,
    QWidget *w,
    const QPoint *pos,
    qdesigner_internal::FormWindowBase::HighlightMode mode) {
  self->highlightWidget(w, *pos, mode);
}

#if QT_CONFIG(clipboard)
//  void qdesigner_internal::FormWindowBase::paste(PasteMode pasteMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase5pasteENS0_9PasteModeE(
    qdesigner_internal::FormWindowBase *self,
    qdesigner_internal::FormWindowBase::PasteMode pasteMode) {
  self->paste(pasteMode);
}
#endif  // QT_CONFIG(clipboard)

//  QEditorFormBuilder
//      *qdesigner_internal::FormWindowBase::createFormBuilder()
extern "C" Q_DECL_EXPORT
qdesigner_internal::QEditorFormBuilder *ritual_ZN18qdesigner_internal14FormWindowBase17createFormBuilderEv(
    qdesigner_internal::FormWindowBase *self) {
  return self->createFormBuilder();
}

//  bool qdesigner_internal::FormWindowBase::blockSelectionChanged(bool
//      blocked)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14FormWindowBase21blockSelectionChangedEb(
    qdesigner_internal::FormWindowBase *self,
    bool blocked) {
  return self->blockSelectionChanged(blocked);
}

//  DesignerPixmapCache *qdesigner_internal::FormWindowBase::pixmapCache()
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerPixmapCache *ritual_ZNK18qdesigner_internal14FormWindowBase11pixmapCacheEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->pixmapCache();
}

//  DesignerIconCache *qdesigner_internal::FormWindowBase::iconCache() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerIconCache *ritual_ZNK18qdesigner_internal14FormWindowBase9iconCacheEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->iconCache();
}

//  QtResourceSet *qdesigner_internal::FormWindowBase::resourceSet() const
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZNK18qdesigner_internal14FormWindowBase11resourceSetEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->resourceSet();
}

//  void qdesigner_internal::FormWindowBase::setResourceSet(QtResourceSet
//      *resourceSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase14setResourceSetEP13QtResourceSet(
    qdesigner_internal::FormWindowBase *self,
    QtResourceSet *resourceSet) {
  self->setResourceSet(resourceSet);
}

//  void qdesigner_internal::FormWindowBase::addReloadableProperty(QDesignerP
//      ropertySheet *sheet, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase21addReloadablePropertyEP22QDesignerPropertySheeti(
    qdesigner_internal::FormWindowBase *self,
    QDesignerPropertySheet *sheet,
    int index) {
  self->addReloadableProperty(sheet, index);
}

//  void qdesigner_internal::FormWindowBase::removeReloadableProperty(QDesign
//      erPropertySheet *sheet, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase24removeReloadablePropertyEP22QDesignerPropertySheeti(
    qdesigner_internal::FormWindowBase *self,
    QDesignerPropertySheet *sheet,
    int index) {
  self->removeReloadableProperty(sheet, index);
}

//  void qdesigner_internal::FormWindowBase::addReloadablePropertySheet(QDesi
//      gnerPropertySheet *sheet, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase26addReloadablePropertySheetEP22QDesignerPropertySheetP7QObject(
    qdesigner_internal::FormWindowBase *self,
    QDesignerPropertySheet *sheet,
    QObject *object) {
  self->addReloadablePropertySheet(sheet, object);
}

//  void qdesigner_internal::FormWindowBase::reloadProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase16reloadPropertiesEv(
    qdesigner_internal::FormWindowBase *self) {
  self->reloadProperties();
}

//  void qdesigner_internal::FormWindowBase::emitWidgetRemoved(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase17emitWidgetRemovedEP7QWidget(
    qdesigner_internal::FormWindowBase *self,
    QWidget *w) {
  self->emitWidgetRemoved(w);
}

//  void qdesigner_internal::FormWindowBase::emitObjectRemoved(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase17emitObjectRemovedEP7QObject(
    qdesigner_internal::FormWindowBase *self,
    QObject *o) {
  self->emitObjectRemoved(o);
}

//  DeviceProfile qdesigner_internal::FormWindowBase::deviceProfile() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZNK18qdesigner_internal14FormWindowBase13deviceProfileEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new qdesigner_internal::DeviceProfile(self->deviceProfile());
}

//  QString qdesigner_internal::FormWindowBase::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal14FormWindowBase9styleNameEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new QString(self->styleName());
}

//  QString qdesigner_internal::FormWindowBase::deviceProfileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal14FormWindowBase17deviceProfileNameEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new QString(self->deviceProfileName());
}

//  void qdesigner_internal::FormWindowBase::setLineTerminatorMode(LineTermin
//      atorMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase21setLineTerminatorModeENS0_18LineTerminatorModeE(
    qdesigner_internal::FormWindowBase *self,
    qdesigner_internal::FormWindowBase::LineTerminatorMode mode) {
  self->setLineTerminatorMode(mode);
}

//  LineTerminatorMode
//      qdesigner_internal::FormWindowBase::lineTerminatorMode() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormWindowBase::LineTerminatorMode ritual_ZNK18qdesigner_internal14FormWindowBase18lineTerminatorModeEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->lineTerminatorMode();
}

//  bool qdesigner_internal::FormWindowBase::useIdBasedTranslations() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal14FormWindowBase22useIdBasedTranslationsEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->useIdBasedTranslations();
}

//  void qdesigner_internal::FormWindowBase::setUseIdBasedTranslations(bool
//      v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase25setUseIdBasedTranslationsEb(
    qdesigner_internal::FormWindowBase *self,
    bool v) {
  self->setUseIdBasedTranslations(v);
}

//  QString qdesigner_internal::FormWindowBase::idBasedTranslationLabel()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal14FormWindowBase23idBasedTranslationLabelEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new QString(self->idBasedTranslationLabel());
}

//  void qdesigner_internal::FormWindowBase::setIdBasedTranslationLabel(const
//      QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase26setIdBasedTranslationLabelERK7QString(
    qdesigner_internal::FormWindowBase *self,
    const QString *a0) {
  self->setIdBasedTranslationLabel(*a0);
}

//  bool qdesigner_internal::FormWindowBase::connectSlotsByName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal14FormWindowBase18connectSlotsByNameEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->connectSlotsByName();
}

//  void qdesigner_internal::FormWindowBase::setConnectSlotsByName(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase21setConnectSlotsByNameEb(
    qdesigner_internal::FormWindowBase *self,
    bool v) {
  self->setConnectSlotsByName(v);
}

//  void
//      qdesigner_internal::FormWindowBase::resourceSetActivated(QtResourceSe
//      t *resourceSet, bool resourceSetChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase20resourceSetActivatedEP13QtResourceSetb(
    qdesigner_internal::FormWindowBase *self,
    QtResourceSet *resourceSet,
    bool resourceSetChanged) {
  self->resourceSetActivated(resourceSet, resourceSetChanged);
}

//  void qdesigner_internal::FormWindowBase::triggerDefaultAction(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase20triggerDefaultActionEP7QWidget(
    qdesigner_internal::FormWindowBase *self,
    QWidget *w) {
  self->triggerDefaultAction(w);
}

//  void qdesigner_internal::FormWindowBase::sheetDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase14sheetDestroyedEP7QObject(
    qdesigner_internal::FormWindowBase *self,
    QObject *object) {
  self->sheetDestroyed(object);
}

//  void qdesigner_internal::FormWindowBase::syncGridFeature()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase15syncGridFeatureEv(
    qdesigner_internal::FormWindowBase *self) {
  self->syncGridFeature();
}

//  void
//      qdesigner_internal::FormWindowBase::connectSheet(QDesignerPropertyShe
//      et *sheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase12connectSheetEP22QDesignerPropertySheet(
    qdesigner_internal::FormWindowBase *self,
    QDesignerPropertySheet *sheet) {
  self->connectSheet(sheet);
}

//  void qdesigner_internal::FormWindowBase::disconnectSheet(QDesignerPropert
//      ySheet *sheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormWindowBase15disconnectSheetEP22QDesignerPropertySheet(
    qdesigner_internal::FormWindowBase *self,
    QDesignerPropertySheet *sheet) {
  self->disconnectSheet(sheet);
}

//  a Python function taken by a Cuteqdesigner_internal_FormWindowBase, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_FormWindowBase(
    qdesigner_internal::FormWindowBase *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_FormWindowBase *>(self)->take(key, call);
}

//  QPoint qdesigner_internal::FormWindowBase::grid() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK18qdesigner_internal14FormWindowBase4gridEv(
    const qdesigner_internal::FormWindowBase *self) {
  return new QPoint(self->qdesigner_internal::FormWindowBase::grid());
}

//  void qdesigner_internal::FormWindowBase::setGrid(const QPoint &grid)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14FormWindowBase7setGridERK6QPoint(
    qdesigner_internal::FormWindowBase *self,
    const QPoint *grid) {
  self->qdesigner_internal::FormWindowBase::setGrid(*grid);
}

//  bool qdesigner_internal::FormWindowBase::hasFeature(Feature f) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18qdesigner_internal14FormWindowBase10hasFeatureE6QFlagsIN28QDesignerFormWindowInterface11FeatureFlagEE(
    const qdesigner_internal::FormWindowBase *self,
    int f) {
  return self->qdesigner_internal::FormWindowBase::hasFeature(
      QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(f));
}

//  Feature qdesigner_internal::FormWindowBase::features() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14FormWindowBase8featuresEv(
    const qdesigner_internal::FormWindowBase *self) {
  return static_cast<int>(
      self->qdesigner_internal::FormWindowBase::features().toInt());
}

//  void qdesigner_internal::FormWindowBase::setFeatures(Feature f)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14FormWindowBase11setFeaturesE6QFlagsIN28QDesignerFormWindowInterface11FeatureFlagEE(
    qdesigner_internal::FormWindowBase *self,
    int f) {
  self->qdesigner_internal::FormWindowBase::setFeatures(
      QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(f));
}

//  ResourceFileSaveMode
//      qdesigner_internal::FormWindowBase::resourceFileSaveMode() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface::ResourceFileSaveMode ritual_own_ZNK18qdesigner_internal14FormWindowBase20resourceFileSaveModeEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->qdesigner_internal::FormWindowBase::resourceFileSaveMode();
}

//  void qdesigner_internal::FormWindowBase::setResourceFileSaveMode(Resource
//      FileSaveMode behavior)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14FormWindowBase23setResourceFileSaveModeEN28QDesignerFormWindowInterface20ResourceFileSaveModeE(
    qdesigner_internal::FormWindowBase *self,
    QDesignerFormWindowInterface::ResourceFileSaveMode behavior) {
  self->qdesigner_internal::FormWindowBase::setResourceFileSaveMode(
      behavior);
}

//  QMenu *qdesigner_internal::FormWindowBase::initializePopupMenu(QWidget
//      *managedWidget)
extern "C" Q_DECL_EXPORT
QMenu *ritual_own_ZN18qdesigner_internal14FormWindowBase19initializePopupMenuEP7QWidget(
    qdesigner_internal::FormWindowBase *self,
    QWidget *managedWidget) {
  return self->qdesigner_internal::FormWindowBase::initializePopupMenu(
      managedWidget);
}

//  QtResourceSet *qdesigner_internal::FormWindowBase::resourceSet() const
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_own_ZNK18qdesigner_internal14FormWindowBase11resourceSetEv(
    const qdesigner_internal::FormWindowBase *self) {
  return self->qdesigner_internal::FormWindowBase::resourceSet();
}

//  void qdesigner_internal::FormWindowBase::setResourceSet(QtResourceSet
//      *resourceSet)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14FormWindowBase14setResourceSetEP13QtResourceSet(
    qdesigner_internal::FormWindowBase *self,
    QtResourceSet *resourceSet) {
  self->qdesigner_internal::FormWindowBase::setResourceSet(resourceSet);
}
