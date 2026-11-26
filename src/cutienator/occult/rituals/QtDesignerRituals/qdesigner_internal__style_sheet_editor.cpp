//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/stylesheeteditor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/stylesheeteditor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::StyleSheetEditor that Python can take functions over in. Every qdesigner_internal::StyleSheetEditor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textedit)
typedef const QVariant * (*Cuteqdesigner_internal_StyleSheetEditorCall0)(const void *, int, const QUrl *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef const QVariant * (*Cuteqdesigner_internal_StyleSheetEditorCall1)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef bool (*Cuteqdesigner_internal_StyleSheetEditorCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall3)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall4)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall5)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall6)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall7)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall10)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef bool (*Cuteqdesigner_internal_StyleSheetEditorCall12)(const void *, bool, int *);
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall14)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall15)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall16)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall17)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall18)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall20)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall21)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
typedef void * (*Cuteqdesigner_internal_StyleSheetEditorCall23)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef bool (*Cuteqdesigner_internal_StyleSheetEditorCall24)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall25)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall26)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall27)(const void *, int, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall28)(const void *, const QTextCursor *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*Cuteqdesigner_internal_StyleSheetEditorCall29)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*Cuteqdesigner_internal_StyleSheetEditorCall30)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall31)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*Cuteqdesigner_internal_StyleSheetEditorCall32)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*Cuteqdesigner_internal_StyleSheetEditorCall33)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*Cuteqdesigner_internal_StyleSheetEditorCall34)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall35)(const void *, QStyleOptionFrame *, int *);
typedef int (*Cuteqdesigner_internal_StyleSheetEditorCall36)(const void *, int *);
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall37)(const void *, bool, int *);
typedef int (*Cuteqdesigner_internal_StyleSheetEditorCall38)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_StyleSheetEditorCall39)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_StyleSheetEditorCall40)(const void *, int *);
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall41)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall42)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall43)(const void *, QMoveEvent *, int *);
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall44)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall45)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall46)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall47)(const void *, QHideEvent *, int *);
typedef int (*Cuteqdesigner_internal_StyleSheetEditorCall48)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall49)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_StyleSheetEditorCall50)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_StyleSheetEditorCall51)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall52)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall53)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall54)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_StyleSheetEditorCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_StyleSheetEditor : public qdesigner_internal::StyleSheetEditor {
public:
  using qdesigner_internal::StyleSheetEditor::StyleSheetEditor;
  void *taken[56] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit12loadResourceEiRK4QUrl")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK9QTextEdit27createMimeDataFromSelectionEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK9QTextEdit21canInsertFromMimeDataEPK9QMimeData")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit18insertFromMimeDataEPK9QMimeData")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit15doSetTextCursorERK11QTextCursor")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[44] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[51] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(textedit)
  //  QVariant QTextEdit::loadResource(int type, const QUrl &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall0 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall0>(taken[0]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QTextEdit::loadResource(type, name);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall1 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QTextEdit::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(textedit)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
  //  bool QTextEdit::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall2 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QTextEdit::event(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
  //  void QTextEdit::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall3 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::timerEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(textedit)
  //  void QTextEdit::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall4 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::keyPressEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall5 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall6 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall6>(taken[6]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::resizeEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall7 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::paintEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall8 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mousePressEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall9 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall10 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
  void mouseDoubleClickEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall11 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseDoubleClickEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  bool QTextEdit::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall12 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall12>(taken[12]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QTextEdit::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(textedit)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
  //  void QTextEdit::contextMenuEvent(QContextMenuEvent *e)
  void contextMenuEvent(QContextMenuEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall13 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::contextMenuEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dragEnterEvent(QDragEnterEvent *e)
  void dragEnterEvent(QDragEnterEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall14 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dragEnterEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall15 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall16 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall17 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dropEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(textedit)
  //  void QTextEdit::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall18 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::focusInEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall19 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::focusOutEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall20 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTextEdit::showEvent(a0);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall21 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall21>(taken[21]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::changeEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
  //  void QTextEdit::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall22 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall22>(taken[22]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::wheelEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(textedit)
  //  QMimeData *QTextEdit::createMimeDataFromSelection() const
  QMimeData *createMimeDataFromSelection() const override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall23 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QTextEdit::createMimeDataFromSelection();
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  bool QTextEdit::canInsertFromMimeData(const QMimeData *source) const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall24 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall24>(taken[24]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QTextEdit::canInsertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::insertFromMimeData(const QMimeData *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall25 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall25>(taken[25]);
      call(this, source, &handled);
      if (handled) return;
    }
    QTextEdit::insertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall26 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTextEdit::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
  //  void QTextEdit::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall27 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall27>(taken[27]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QTextEdit::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(textedit)
  //  void QTextEdit::doSetTextCursor(const QTextCursor &cursor)
  void doSetTextCursor(const QTextCursor &cursor) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall28 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall28>(taken[28]);
      call(this, &cursor, &handled);
      if (handled) return;
    }
    QTextEdit::doSetTextCursor(cursor);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall29 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall29>(taken[29]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall30 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall30>(taken[30]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall31 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall31>(taken[31]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall32 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
  bool viewportEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall33 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall33>(taken[33]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall34 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall34>(taken[34]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall35 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall35>(taken[35]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall36 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall36>(taken[36]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall37 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall37>(taken[37]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall38 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall38>(taken[38]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall39 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall39>(taken[39]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall40 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall41 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall42 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall43 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall44 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall45 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall46 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall47 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[48]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall48 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall48>(taken[48]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[49]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall49 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall49>(taken[49]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[50]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall50 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall50>(taken[50]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[51]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall51 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall51>(taken[51]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall52 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall53 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall54 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[55]) {
      int handled = 0;
      Cuteqdesigner_internal_StyleSheetEditorCall55 call = reinterpret_cast<Cuteqdesigner_internal_StyleSheetEditorCall55>(taken[55]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::StyleSheetEditor::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal16StyleSheetEditor10metaObjectEv(
    const qdesigner_internal::StyleSheetEditor *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::StyleSheetEditor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal16StyleSheetEditor11qt_metacastEPKc(
    qdesigner_internal::StyleSheetEditor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::StyleSheetEditor::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal16StyleSheetEditor11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::StyleSheetEditor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::StyleSheetEditor::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal16StyleSheetEditor2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::StyleSheetEditor::tr(s, c, n));
}

//  qdesigner_internal::StyleSheetEditor::StyleSheetEditor(QWidget *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::StyleSheetEditor *ritual_ZN18qdesigner_internal16StyleSheetEditorC1EP7QWidget(
    QWidget *parent) {
  return new Cuteqdesigner_internal_StyleSheetEditor(parent);
}

//  a Python function taken by a Cuteqdesigner_internal_StyleSheetEditor, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_StyleSheetEditor(
    qdesigner_internal::StyleSheetEditor *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_StyleSheetEditor *>(self)->take(key, call);
}
