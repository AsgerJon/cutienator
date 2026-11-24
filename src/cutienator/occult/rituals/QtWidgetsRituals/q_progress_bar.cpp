//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qprogressbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
#include <QtWidgets/qprogressbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QProgressBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQProgressBar : QProgressBar {
  using QProgressBar::event;
  using QProgressBar::paintEvent;
  using QProgressBar::initStyleOption;
};

//  A QProgressBar that Python can take functions over in. Every QProgressBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(progressbar)
typedef QString * (*CuteQProgressBarCall0)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
typedef const QSize * (*CuteQProgressBarCall1)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
typedef const QSize * (*CuteQProgressBarCall2)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(progressbar)
typedef bool (*CuteQProgressBarCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(progressbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(progressbar)
typedef void (*CuteQProgressBarCall4)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
typedef void (*CuteQProgressBarCall5)(const void *, QStyleOptionProgressBar *, int *);
#endif  // QT_CONFIG(progressbar)
typedef int (*CuteQProgressBarCall6)(const void *, int *);
typedef void (*CuteQProgressBarCall7)(const void *, bool, int *);
typedef int (*CuteQProgressBarCall8)(const void *, int, int *);
typedef bool (*CuteQProgressBarCall9)(const void *, int *);
typedef void * (*CuteQProgressBarCall10)(const void *, int *);
typedef void (*CuteQProgressBarCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressBarCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressBarCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressBarCall14)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQProgressBarCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQProgressBarCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQProgressBarCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQProgressBarCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQProgressBarCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQProgressBarCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQProgressBarCall21)(const void *, QEvent *, int *);
typedef void (*CuteQProgressBarCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQProgressBarCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQProgressBarCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQProgressBarCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQProgressBarCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQProgressBarCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQProgressBarCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQProgressBarCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQProgressBarCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQProgressBarCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQProgressBarCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQProgressBarCall33)(const void *, QHideEvent *, int *);
typedef void (*CuteQProgressBarCall34)(const void *, QEvent *, int *);
typedef int (*CuteQProgressBarCall35)(const void *, int, int *);
typedef void (*CuteQProgressBarCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQProgressBarCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQProgressBarCall38)(const void *, int *);
typedef void (*CuteQProgressBarCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQProgressBarCall40)(const void *, int, int *);
typedef bool (*CuteQProgressBarCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQProgressBarCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProgressBarCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProgressBarCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProgressBarCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProgressBarCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProgressBarCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQProgressBar : public QProgressBar {
public:
  using QProgressBar::QProgressBar;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK12QProgressBar4textEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK12QProgressBar15initStyleOptionEP23QStyleOptionProgressBar")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
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

#if QT_CONFIG(progressbar)
  //  QString QProgressBar::text() const
  QString text() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQProgressBarCall0 call = reinterpret_cast<CuteQProgressBarCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QProgressBar::text();
  }
#endif  // QT_CONFIG(progressbar)

#if QT_CONFIG(progressbar)
  //  QSize QProgressBar::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQProgressBarCall1 call = reinterpret_cast<CuteQProgressBarCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QProgressBar::sizeHint();
  }
#endif  // QT_CONFIG(progressbar)

#if QT_CONFIG(progressbar)
  //  QSize QProgressBar::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQProgressBarCall2 call = reinterpret_cast<CuteQProgressBarCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QProgressBar::minimumSizeHint();
  }
#endif  // QT_CONFIG(progressbar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(progressbar)
  //  bool QProgressBar::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQProgressBarCall3 call = reinterpret_cast<CuteQProgressBarCall3>(taken[3]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QProgressBar::event(e);
  }
#endif  // QT_CONFIG(progressbar)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(progressbar)
  //  void QProgressBar::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQProgressBarCall4 call = reinterpret_cast<CuteQProgressBarCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QProgressBar::paintEvent(a0);
  }
#endif  // QT_CONFIG(progressbar)

#if QT_CONFIG(progressbar)
  //  void QProgressBar::initStyleOption(QStyleOptionProgressBar *option)
  //      const
  void initStyleOption(QStyleOptionProgressBar *option) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQProgressBarCall5 call = reinterpret_cast<CuteQProgressBarCall5>(taken[5]);
      call(this, option, &handled);
      if (handled) return;
    }
    QProgressBar::initStyleOption(option);
  }
#endif  // QT_CONFIG(progressbar)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQProgressBarCall6 call = reinterpret_cast<CuteQProgressBarCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[7]) {
      int handled = 0;
      CuteQProgressBarCall7 call = reinterpret_cast<CuteQProgressBarCall7>(taken[7]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQProgressBarCall8 call = reinterpret_cast<CuteQProgressBarCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQProgressBarCall9 call = reinterpret_cast<CuteQProgressBarCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQProgressBarCall10 call = reinterpret_cast<CuteQProgressBarCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQProgressBarCall11 call = reinterpret_cast<CuteQProgressBarCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQProgressBarCall12 call = reinterpret_cast<CuteQProgressBarCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQProgressBarCall13 call = reinterpret_cast<CuteQProgressBarCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQProgressBarCall14 call = reinterpret_cast<CuteQProgressBarCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQProgressBarCall15 call = reinterpret_cast<CuteQProgressBarCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQProgressBarCall16 call = reinterpret_cast<CuteQProgressBarCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQProgressBarCall17 call = reinterpret_cast<CuteQProgressBarCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQProgressBarCall18 call = reinterpret_cast<CuteQProgressBarCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQProgressBarCall19 call = reinterpret_cast<CuteQProgressBarCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQProgressBarCall20 call = reinterpret_cast<CuteQProgressBarCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQProgressBarCall21 call = reinterpret_cast<CuteQProgressBarCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQProgressBarCall22 call = reinterpret_cast<CuteQProgressBarCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQProgressBarCall23 call = reinterpret_cast<CuteQProgressBarCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQProgressBarCall24 call = reinterpret_cast<CuteQProgressBarCall24>(taken[24]);
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
      CuteQProgressBarCall25 call = reinterpret_cast<CuteQProgressBarCall25>(taken[25]);
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
      CuteQProgressBarCall26 call = reinterpret_cast<CuteQProgressBarCall26>(taken[26]);
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
      CuteQProgressBarCall27 call = reinterpret_cast<CuteQProgressBarCall27>(taken[27]);
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
      CuteQProgressBarCall28 call = reinterpret_cast<CuteQProgressBarCall28>(taken[28]);
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
      CuteQProgressBarCall29 call = reinterpret_cast<CuteQProgressBarCall29>(taken[29]);
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
      CuteQProgressBarCall30 call = reinterpret_cast<CuteQProgressBarCall30>(taken[30]);
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
      CuteQProgressBarCall31 call = reinterpret_cast<CuteQProgressBarCall31>(taken[31]);
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
      CuteQProgressBarCall32 call = reinterpret_cast<CuteQProgressBarCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQProgressBarCall33 call = reinterpret_cast<CuteQProgressBarCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQProgressBarCall34 call = reinterpret_cast<CuteQProgressBarCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQProgressBarCall35 call = reinterpret_cast<CuteQProgressBarCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQProgressBarCall36 call = reinterpret_cast<CuteQProgressBarCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQProgressBarCall37 call = reinterpret_cast<CuteQProgressBarCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQProgressBarCall38 call = reinterpret_cast<CuteQProgressBarCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQProgressBarCall39 call = reinterpret_cast<CuteQProgressBarCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQProgressBarCall40 call = reinterpret_cast<CuteQProgressBarCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQProgressBarCall41 call = reinterpret_cast<CuteQProgressBarCall41>(taken[41]);
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
      CuteQProgressBarCall42 call = reinterpret_cast<CuteQProgressBarCall42>(taken[42]);
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
      CuteQProgressBarCall43 call = reinterpret_cast<CuteQProgressBarCall43>(taken[43]);
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
      CuteQProgressBarCall44 call = reinterpret_cast<CuteQProgressBarCall44>(taken[44]);
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
      CuteQProgressBarCall45 call = reinterpret_cast<CuteQProgressBarCall45>(taken[45]);
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
      CuteQProgressBarCall46 call = reinterpret_cast<CuteQProgressBarCall46>(taken[46]);
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
      CuteQProgressBarCall47 call = reinterpret_cast<CuteQProgressBarCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QProgressBar10metaObjectEv(
    const QProgressBar *self) {
  return self->metaObject();
}

//  QString QProgressBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QProgressBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProgressBar::tr(s, c, n));
}

//  QProgressBar::QProgressBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QProgressBar *ritual_ZN12QProgressBarC1EP7QWidget(QWidget *parent) {
  return new CuteQProgressBar(parent);
}

//  QProgressBar::~QProgressBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBarD1Ev(QProgressBar *self) {
  delete self;
}

//  int QProgressBar::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar7minimumEv(const QProgressBar *self) {
  return self->minimum();
}

//  int QProgressBar::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar7maximumEv(const QProgressBar *self) {
  return self->maximum();
}

//  int QProgressBar::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar5valueEv(const QProgressBar *self) {
  return self->value();
}

//  QString QProgressBar::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QProgressBar4textEv(const QProgressBar *self) {
  return new QString(self->text());
}

//  void QProgressBar::setTextVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar14setTextVisibleEb(
    QProgressBar *self,
    bool visible) {
  self->setTextVisible(visible);
}

//  bool QProgressBar::isTextVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QProgressBar13isTextVisibleEv(const QProgressBar *self) {
  return self->isTextVisible();
}

//  Qt::Alignment QProgressBar::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar9alignmentEv(const QProgressBar *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QProgressBar::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QProgressBar *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QSize QProgressBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QProgressBar8sizeHintEv(const QProgressBar *self) {
  return new QSize(self->sizeHint());
}

//  QSize QProgressBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QProgressBar15minimumSizeHintEv(
    const QProgressBar *self) {
  return new QSize(self->minimumSizeHint());
}

//  Qt::Orientation QProgressBar::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK12QProgressBar11orientationEv(
    const QProgressBar *self) {
  return self->orientation();
}

//  void QProgressBar::setInvertedAppearance(bool invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar21setInvertedAppearanceEb(
    QProgressBar *self,
    bool invert) {
  self->setInvertedAppearance(invert);
}

//  bool QProgressBar::invertedAppearance() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QProgressBar18invertedAppearanceEv(
    const QProgressBar *self) {
  return self->invertedAppearance();
}

//  void QProgressBar::setTextDirection(QProgressBar::Direction
//      textDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar16setTextDirectionENS_9DirectionE(
    QProgressBar *self,
    QProgressBar::Direction textDirection) {
  self->setTextDirection(textDirection);
}

//  QProgressBar::Direction QProgressBar::textDirection() const
extern "C" Q_DECL_EXPORT
QProgressBar::Direction ritual_ZNK12QProgressBar13textDirectionEv(
    const QProgressBar *self) {
  return self->textDirection();
}

//  void QProgressBar::setFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar9setFormatERK7QString(
    QProgressBar *self,
    const QString *format) {
  self->setFormat(*format);
}

//  void QProgressBar::resetFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar11resetFormatEv(QProgressBar *self) {
  self->resetFormat();
}

//  QString QProgressBar::format() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QProgressBar6formatEv(const QProgressBar *self) {
  return new QString(self->format());
}

//  void QProgressBar::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar5resetEv(QProgressBar *self) {
  self->reset();
}

//  void QProgressBar::setRange(int minimum, int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar8setRangeEii(
    QProgressBar *self,
    int minimum,
    int maximum) {
  self->setRange(minimum, maximum);
}

//  void QProgressBar::setMinimum(int minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar10setMinimumEi(QProgressBar *self, int minimum) {
  self->setMinimum(minimum);
}

//  void QProgressBar::setMaximum(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar10setMaximumEi(QProgressBar *self, int maximum) {
  self->setMaximum(maximum);
}

//  void QProgressBar::setValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar8setValueEi(QProgressBar *self, int value) {
  self->setValue(value);
}

//  void QProgressBar::setOrientation(Qt::Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar14setOrientationEN2Qt11OrientationE(
    QProgressBar *self,
    Qt::Orientation a0) {
  self->setOrientation(a0);
}

//  bool QProgressBar::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QProgressBar5eventEP6QEvent(QProgressBar *self, QEvent *e) {
  return self->event(e);
}

//  void QProgressBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar10paintEventEP11QPaintEvent(
    QProgressBar *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QProgressBar::initStyleOption(QStyleOptionProgressBar *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QProgressBar15initStyleOptionEP23QStyleOptionProgressBar(
    const QProgressBar *self,
    QStyleOptionProgressBar *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQProgressBar, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProgressBar(
    QProgressBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProgressBar *>(self)->take(key, call);
}

//  QString QProgressBar::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK12QProgressBar4textEv(const QProgressBar *self) {
  return new QString(self->QProgressBar::text());
}

//  QSize QProgressBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QProgressBar8sizeHintEv(const QProgressBar *self) {
  return new QSize(self->QProgressBar::sizeHint());
}

//  QSize QProgressBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QProgressBar15minimumSizeHintEv(
    const QProgressBar *self) {
  return new QSize(self->QProgressBar::minimumSizeHint());
}

//  bool QProgressBar::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QProgressBar5eventEP6QEvent(
    QProgressBar *self,
    QEvent *e) {
  return static_cast<OwnQProgressBar *>(self)->OwnQProgressBar::event(e);
}

//  void QProgressBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QProgressBar10paintEventEP11QPaintEvent(
    QProgressBar *self,
    QPaintEvent *a0) {
  static_cast<OwnQProgressBar *>(self)->OwnQProgressBar::paintEvent(a0);
}

//  void QProgressBar::initStyleOption(QStyleOptionProgressBar *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QProgressBar15initStyleOptionEP23QStyleOptionProgressBar(
    const QProgressBar *self,
    QStyleOptionProgressBar *option) {
  static_cast<const OwnQProgressBar *>(self)->OwnQProgressBar::initStyleOption(
      option);
}

#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(progressbar)
