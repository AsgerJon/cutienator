//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractactioneditor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDesigner/abstractactioneditor.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerActionEditorInterface that Python can take functions over in. Every QDesignerActionEditorInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerActionEditorInterfaceCall0)(const void *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall1)(const void *, QAction *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall2)(const void *, QAction *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall3)(const void *, QDesignerFormWindowInterface *, int *);
typedef int (*CuteQDesignerActionEditorInterfaceCall4)(const void *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall5)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerActionEditorInterfaceCall6)(const void *, int *);
typedef const QSize * (*CuteQDesignerActionEditorInterfaceCall7)(const void *, int *);
typedef int (*CuteQDesignerActionEditorInterfaceCall8)(const void *, int, int *);
typedef bool (*CuteQDesignerActionEditorInterfaceCall9)(const void *, int *);
typedef void * (*CuteQDesignerActionEditorInterfaceCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerActionEditorInterfaceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerActionEditorInterfaceCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall15)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerActionEditorInterfaceCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerActionEditorInterfaceCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall21)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall22)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall23)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall25)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall26)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerActionEditorInterfaceCall27)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerActionEditorInterfaceCall28)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerActionEditorInterfaceCall29)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerActionEditorInterfaceCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerActionEditorInterfaceCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerActionEditorInterfaceCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerActionEditorInterfaceCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerActionEditorInterfaceCall34)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall35)(const void *, QHideEvent *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall36)(const void *, QEvent *, int *);
typedef int (*CuteQDesignerActionEditorInterfaceCall37)(const void *, int, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall38)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerActionEditorInterfaceCall39)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerActionEditorInterfaceCall40)(const void *, int *);
typedef void (*CuteQDesignerActionEditorInterfaceCall41)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerActionEditorInterfaceCall42)(const void *, int, int *);
typedef bool (*CuteQDesignerActionEditorInterfaceCall43)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerActionEditorInterfaceCall44)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerActionEditorInterfaceCall45)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerActionEditorInterfaceCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerActionEditorInterfaceCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerActionEditorInterfaceCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerActionEditorInterfaceCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerActionEditorInterface : public QDesignerActionEditorInterface {
public:
  using QDesignerActionEditorInterface::QDesignerActionEditorInterface;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK30QDesignerActionEditorInterface4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerActionEditorInterface12manageActionEP7QAction")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerActionEditorInterface14unmanageActionEP7QAction")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerActionEditorInterface13setFormWindowEP28QDesignerFormWindowInterface")) {
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

  //  QDesignerFormEditorInterface *QDesignerActionEditorInterface::core()
  //      const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall0 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return QDesignerActionEditorInterface::core();
  }

  //  void QDesignerActionEditorInterface::manageAction(QAction *action)
  void manageAction(QAction *action) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall1 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall1>(taken[1]);
      call(this, action, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerActionEditorInterface::unmanageAction(QAction *action)
  void unmanageAction(QAction *action) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall2 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall2>(taken[2]);
      call(this, action, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerActionEditorInterface::setFormWindow(QDesignerFormWindo
  //      wInterface *formWindow)
  void setFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall3 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall3>(taken[3]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall4 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall5 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall5>(taken[5]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall6 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall7 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall8 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall9 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall10 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall10>(taken[10]);
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
      CuteQDesignerActionEditorInterfaceCall11 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall11>(taken[11]);
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
      CuteQDesignerActionEditorInterfaceCall12 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall13 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall14 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall15 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall15>(taken[15]);
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
      CuteQDesignerActionEditorInterfaceCall16 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall16>(taken[16]);
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
      CuteQDesignerActionEditorInterfaceCall17 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall18 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall19 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall20 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall21 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall22 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall23 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall24 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall25 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall26 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall26>(taken[26]);
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
      CuteQDesignerActionEditorInterfaceCall27 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall27>(taken[27]);
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
      CuteQDesignerActionEditorInterfaceCall28 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall28>(taken[28]);
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
      CuteQDesignerActionEditorInterfaceCall29 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall29>(taken[29]);
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
      CuteQDesignerActionEditorInterfaceCall30 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall30>(taken[30]);
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
      CuteQDesignerActionEditorInterfaceCall31 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall31>(taken[31]);
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
      CuteQDesignerActionEditorInterfaceCall32 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall32>(taken[32]);
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
      CuteQDesignerActionEditorInterfaceCall33 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall33>(taken[33]);
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
      CuteQDesignerActionEditorInterfaceCall34 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall35 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall36 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall37 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall38 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall39 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall40 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall41 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall42 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDesignerActionEditorInterfaceCall43 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall43>(taken[43]);
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
      CuteQDesignerActionEditorInterfaceCall44 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall44>(taken[44]);
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
      CuteQDesignerActionEditorInterfaceCall45 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall45>(taken[45]);
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
      CuteQDesignerActionEditorInterfaceCall46 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall46>(taken[46]);
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
      CuteQDesignerActionEditorInterfaceCall47 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall47>(taken[47]);
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
      CuteQDesignerActionEditorInterfaceCall48 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall48>(taken[48]);
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
      CuteQDesignerActionEditorInterfaceCall49 call = reinterpret_cast<CuteQDesignerActionEditorInterfaceCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerActionEditorInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QDesignerActionEditorInterface10metaObjectEv(
    const QDesignerActionEditorInterface *self) {
  return self->metaObject();
}

//  void *QDesignerActionEditorInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QDesignerActionEditorInterface11qt_metacastEPKc(
    QDesignerActionEditorInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerActionEditorInterface::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QDesignerActionEditorInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerActionEditorInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerActionEditorInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QDesignerActionEditorInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerActionEditorInterface::tr(s, c, n));
}

//  QDesignerActionEditorInterface::QDesignerActionEditorInterface(QWidget
//      *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDesignerActionEditorInterface *ritual_ZN30QDesignerActionEditorInterfaceC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQDesignerActionEditorInterface(
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDesignerActionEditorInterface::~QDesignerActionEditorInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerActionEditorInterfaceD1Ev(
    QDesignerActionEditorInterface *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerActionEditorInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK30QDesignerActionEditorInterface4coreEv(
    const QDesignerActionEditorInterface *self) {
  return self->core();
}

//  void QDesignerActionEditorInterface::manageAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerActionEditorInterface12manageActionEP7QAction(
    QDesignerActionEditorInterface *self,
    QAction *action) {
  self->manageAction(action);
}

//  void QDesignerActionEditorInterface::unmanageAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerActionEditorInterface14unmanageActionEP7QAction(
    QDesignerActionEditorInterface *self,
    QAction *action) {
  self->unmanageAction(action);
}

//  void QDesignerActionEditorInterface::setFormWindow(QDesignerFormWindowInt
//      erface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerActionEditorInterface13setFormWindowEP28QDesignerFormWindowInterface(
    QDesignerActionEditorInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->setFormWindow(formWindow);
}

//  a Python function taken by a CuteQDesignerActionEditorInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerActionEditorInterface(
    QDesignerActionEditorInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerActionEditorInterface *>(self)->take(key, call);
}

//  QDesignerFormEditorInterface *QDesignerActionEditorInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK30QDesignerActionEditorInterface4coreEv(
    const QDesignerActionEditorInterface *self) {
  return self->QDesignerActionEditorInterface::core();
}
