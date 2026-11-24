//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actioneditor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actioneditor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::ActionEditor that Python can take functions over in. Every qdesigner_internal::ActionEditor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_ActionEditorCall0)(const void *, QDesignerFormWindowInterface *, int *);
typedef void * (*Cuteqdesigner_internal_ActionEditorCall1)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall2)(const void *, QAction *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall3)(const void *, QAction *, int *);
typedef int (*Cuteqdesigner_internal_ActionEditorCall4)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall5)(const void *, bool, int *);
typedef const QSize * (*Cuteqdesigner_internal_ActionEditorCall6)(const void *, int *);
typedef const QSize * (*Cuteqdesigner_internal_ActionEditorCall7)(const void *, int *);
typedef int (*Cuteqdesigner_internal_ActionEditorCall8)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_ActionEditorCall9)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_ActionEditorCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_ActionEditorCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ActionEditorCall12)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall13)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall14)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall15)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_ActionEditorCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_ActionEditorCall17)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall18)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall19)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall20)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall21)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall22)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall23)(const void *, QPaintEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall24)(const void *, QMoveEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall25)(const void *, QResizeEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall26)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*Cuteqdesigner_internal_ActionEditorCall27)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_ActionEditorCall28)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_ActionEditorCall29)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ActionEditorCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ActionEditorCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ActionEditorCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ActionEditorCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ActionEditorCall34)(const void *, QShowEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall35)(const void *, QHideEvent *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall36)(const void *, QEvent *, int *);
typedef int (*Cuteqdesigner_internal_ActionEditorCall37)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall38)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_ActionEditorCall39)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_ActionEditorCall40)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ActionEditorCall41)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*Cuteqdesigner_internal_ActionEditorCall42)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_ActionEditorCall43)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_ActionEditorCall44)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ActionEditorCall45)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ActionEditorCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ActionEditorCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ActionEditorCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ActionEditorCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_ActionEditor : public qdesigner_internal::ActionEditor {
public:
  using qdesigner_internal::ActionEditor::ActionEditor;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QDesignerActionEditorInterface13setFormWindowEP28QDesignerFormWindowInterface")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerActionEditorInterface4coreEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerActionEditorInterface12manageActionEP7QAction")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerActionEditorInterface14unmanageActionEP7QAction")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[26] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[43] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void qdesigner_internal::ActionEditor::setFormWindow(QDesignerFormWin
  //      dowInterface *formWindow)
  void setFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall0 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall0>(taken[0]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
    qdesigner_internal::ActionEditor::setFormWindow(formWindow);
  }

  //  QDesignerFormEditorInterface
  //      *qdesigner_internal::ActionEditor::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall1 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return qdesigner_internal::ActionEditor::core();
  }

  //  void qdesigner_internal::ActionEditor::manageAction(QAction *action)
  void manageAction(QAction *action) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall2 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall2>(taken[2]);
      call(this, action, &handled);
      if (handled) return;
    }
    qdesigner_internal::ActionEditor::manageAction(action);
  }

  //  void qdesigner_internal::ActionEditor::unmanageAction(QAction
  //      *action)
  void unmanageAction(QAction *action) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall3 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall3>(taken[3]);
      call(this, action, &handled);
      if (handled) return;
    }
    qdesigner_internal::ActionEditor::unmanageAction(action);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall4 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall5 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall5>(taken[5]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall6 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall7 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall8 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall9 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall10 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall11 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall12 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall13 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall14 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall15 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall16 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall17 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall18 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall19 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall20 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall21 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall22 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall23 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall24 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall25 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall26 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall27 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall28 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall29 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall30 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall31 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall32 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall33 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall34 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall35 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall36 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall37 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall38 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall39 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall40 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall41 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall42 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall43 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall43>(taken[43]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall44 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall45 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall46 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall47 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall48 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      Cuteqdesigner_internal_ActionEditorCall49 call = reinterpret_cast<Cuteqdesigner_internal_ActionEditorCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::ActionEditor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal12ActionEditor10metaObjectEv(
    const qdesigner_internal::ActionEditor *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ActionEditor::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal12ActionEditor2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ActionEditor::tr(s, c, n));
}

//  ObjectNamingMode qdesigner_internal::ActionEditor::objectNamingMode()
extern "C" Q_DECL_EXPORT
qdesigner_internal::ObjectNamingMode ritual_ZN18qdesigner_internal12ActionEditor16objectNamingModeEv() {
  return qdesigner_internal::ActionEditor::objectNamingMode();
}

//  void
//      qdesigner_internal::ActionEditor::setObjectNamingMode(ObjectNamingMod
//      e n)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12ActionEditor19setObjectNamingModeENS_16ObjectNamingModeE(
    qdesigner_internal::ObjectNamingMode n) {
  qdesigner_internal::ActionEditor::setObjectNamingMode(n);
}

//  a Python function taken by a Cuteqdesigner_internal_ActionEditor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_ActionEditor(
    qdesigner_internal::ActionEditor *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_ActionEditor *>(self)->take(key, call);
}

//  void qdesigner_internal::ActionEditor::setFormWindow(QDesignerFormWindowI
//      nterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal12ActionEditor13setFormWindowEP28QDesignerFormWindowInterface(
    qdesigner_internal::ActionEditor *self,
    QDesignerFormWindowInterface *formWindow) {
  self->qdesigner_internal::ActionEditor::setFormWindow(formWindow);
}

//  QDesignerFormEditorInterface *qdesigner_internal::ActionEditor::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK18qdesigner_internal12ActionEditor4coreEv(
    const qdesigner_internal::ActionEditor *self) {
  return self->qdesigner_internal::ActionEditor::core();
}

//  void qdesigner_internal::ActionEditor::manageAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal12ActionEditor12manageActionEP7QAction(
    qdesigner_internal::ActionEditor *self,
    QAction *action) {
  self->qdesigner_internal::ActionEditor::manageAction(action);
}

//  void qdesigner_internal::ActionEditor::unmanageAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal12ActionEditor14unmanageActionEP7QAction(
    qdesigner_internal::ActionEditor *self,
    QAction *action) {
  self->qdesigner_internal::ActionEditor::unmanageAction(action);
}
