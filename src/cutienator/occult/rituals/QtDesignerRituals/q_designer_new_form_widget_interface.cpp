//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractnewformwidget.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtDesigner/abstractnewformwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerNewFormWidgetInterface that Python can take functions over in. Every QDesignerNewFormWidgetInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDesignerNewFormWidgetInterfaceCall0)(const void *, int *);
typedef QString * (*CuteQDesignerNewFormWidgetInterfaceCall1)(const void *, QString *, int *);
typedef int (*CuteQDesignerNewFormWidgetInterfaceCall2)(const void *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall3)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerNewFormWidgetInterfaceCall4)(const void *, int *);
typedef const QSize * (*CuteQDesignerNewFormWidgetInterfaceCall5)(const void *, int *);
typedef int (*CuteQDesignerNewFormWidgetInterfaceCall6)(const void *, int, int *);
typedef bool (*CuteQDesignerNewFormWidgetInterfaceCall7)(const void *, int *);
typedef void * (*CuteQDesignerNewFormWidgetInterfaceCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerNewFormWidgetInterfaceCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall13)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall14)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall19)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall20)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall21)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall33)(const void *, QHideEvent *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall34)(const void *, QEvent *, int *);
typedef int (*CuteQDesignerNewFormWidgetInterfaceCall35)(const void *, int, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerNewFormWidgetInterfaceCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerNewFormWidgetInterfaceCall38)(const void *, int *);
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerNewFormWidgetInterfaceCall40)(const void *, int, int *);
typedef bool (*CuteQDesignerNewFormWidgetInterfaceCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerNewFormWidgetInterfaceCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerNewFormWidgetInterfaceCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerNewFormWidgetInterface : public QDesignerNewFormWidgetInterface {
public:
  using QDesignerNewFormWidgetInterface::QDesignerNewFormWidgetInterface;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QDesignerNewFormWidgetInterface18hasCurrentTemplateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerNewFormWidgetInterface15currentTemplateEP7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QDesignerNewFormWidgetInterface::hasCurrentTemplate() const
  bool hasCurrentTemplate() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall0 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerNewFormWidgetInterface::currentTemplate(QString
  //      *errorMessage)
  QString currentTemplate(QString *errorMessage) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall1 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall1>(taken[1]);
      QString * given = call(this, errorMessage, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall2 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall3 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall4 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall5 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall6 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall6>(taken[6]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall7 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall8 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall9 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall10 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall11 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall12 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall13 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall14 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall15 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall16 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall17 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall18 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall19 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall20 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall21 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall22 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall23 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall24 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall25 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall26 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall27 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall28 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall29 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall30 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall31 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall32 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall33 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall34 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall35 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall36 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall37 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall38 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall39 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall40 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall41 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall42 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall43 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall44 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall45 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall46 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDesignerNewFormWidgetInterfaceCall47 call = reinterpret_cast<CuteQDesignerNewFormWidgetInterfaceCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerNewFormWidgetInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QDesignerNewFormWidgetInterface10metaObjectEv(
    const QDesignerNewFormWidgetInterface *self) {
  return self->metaObject();
}

//  QString QDesignerNewFormWidgetInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QDesignerNewFormWidgetInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerNewFormWidgetInterface::tr(s, c, n));
}

//  QDesignerNewFormWidgetInterface::~QDesignerNewFormWidgetInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerNewFormWidgetInterfaceD1Ev(
    QDesignerNewFormWidgetInterface *self) {
  delete self;
}

//  bool QDesignerNewFormWidgetInterface::hasCurrentTemplate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QDesignerNewFormWidgetInterface18hasCurrentTemplateEv(
    const QDesignerNewFormWidgetInterface *self) {
  return self->hasCurrentTemplate();
}

//  QString QDesignerNewFormWidgetInterface::currentTemplate(QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QDesignerNewFormWidgetInterface15currentTemplateEP7QString(
    QDesignerNewFormWidgetInterface *self,
    QString *errorMessage) {
  return new QString(self->currentTemplate(errorMessage));
}

//  QDesignerNewFormWidgetInterface *QDesignerNewFormWidgetInterface::createN
//      ewFormWidget(QDesignerFormEditorInterface *core, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerNewFormWidgetInterface *ritual_ZN31QDesignerNewFormWidgetInterface19createNewFormWidgetEP28QDesignerFormEditorInterfaceP7QWidget(
    QDesignerFormEditorInterface *core,
    QWidget *parent) {
  return QDesignerNewFormWidgetInterface::createNewFormWidget(core, parent);
}

//  a Python function taken by a CuteQDesignerNewFormWidgetInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerNewFormWidgetInterface(
    QDesignerNewFormWidgetInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerNewFormWidgetInterface *>(self)->take(key, call);
}
