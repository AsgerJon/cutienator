//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsplitter.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsplitter.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSplitter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSplitter : QSplitter {
  using QSplitter::createHandle;
  using QSplitter::childEvent;
  using QSplitter::event;
  using QSplitter::resizeEvent;
  using QSplitter::changeEvent;
};

//  A QSplitter that Python can take functions over in. Every QSplitter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSplitterCall0)(const void *, int *);
typedef const QSize * (*CuteQSplitterCall1)(const void *, int *);
typedef void * (*CuteQSplitterCall2)(const void *, int *);
typedef void (*CuteQSplitterCall3)(const void *, QChildEvent *, int *);
typedef bool (*CuteQSplitterCall4)(const void *, QEvent *, int *);
typedef void (*CuteQSplitterCall5)(const void *, QResizeEvent *, int *);
typedef void (*CuteQSplitterCall6)(const void *, QEvent *, int *);
typedef void (*CuteQSplitterCall7)(const void *, QPaintEvent *, int *);
typedef void (*CuteQSplitterCall8)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQSplitterCall9)(const void *, int *);
typedef void (*CuteQSplitterCall10)(const void *, bool, int *);
typedef int (*CuteQSplitterCall11)(const void *, int, int *);
typedef bool (*CuteQSplitterCall12)(const void *, int *);
typedef void * (*CuteQSplitterCall13)(const void *, int *);
typedef void (*CuteQSplitterCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSplitterCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSplitterCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSplitterCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSplitterCall18)(const void *, QWheelEvent *, int *);
typedef void (*CuteQSplitterCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSplitterCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSplitterCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSplitterCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSplitterCall23)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSplitterCall24)(const void *, QEvent *, int *);
typedef void (*CuteQSplitterCall25)(const void *, QMoveEvent *, int *);
typedef void (*CuteQSplitterCall26)(const void *, QCloseEvent *, int *);
typedef void (*CuteQSplitterCall27)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQSplitterCall28)(const void *, QTabletEvent *, int *);
typedef void (*CuteQSplitterCall29)(const void *, QActionEvent *, int *);
typedef void (*CuteQSplitterCall30)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQSplitterCall31)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQSplitterCall32)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQSplitterCall33)(const void *, QDropEvent *, int *);
typedef void (*CuteQSplitterCall34)(const void *, QShowEvent *, int *);
typedef void (*CuteQSplitterCall35)(const void *, QHideEvent *, int *);
typedef int (*CuteQSplitterCall36)(const void *, int, int *);
typedef void (*CuteQSplitterCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQSplitterCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQSplitterCall39)(const void *, int *);
typedef void (*CuteQSplitterCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQSplitterCall41)(const void *, int, int *);
typedef bool (*CuteQSplitterCall42)(const void *, bool, int *);
typedef bool (*CuteQSplitterCall43)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQSplitterCall44)(const void *, QTimerEvent *, int *);
typedef void (*CuteQSplitterCall45)(const void *, QEvent *, int *);
typedef void (*CuteQSplitterCall46)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQSplitterCall47)(const void *, const QMetaMethod *, int *);
class CuteQSplitter : public QSplitter {
public:
  using QSplitter::QSplitter;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QSplitter12createHandleEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
    return false;
  }

  //  QSize QSplitter::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSplitterCall0 call = reinterpret_cast<CuteQSplitterCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSplitter::sizeHint();
  }

  //  QSize QSplitter::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplitterCall1 call = reinterpret_cast<CuteQSplitterCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSplitter::minimumSizeHint();
  }

  //  QSplitterHandle *QSplitter::createHandle()
  QSplitterHandle *createHandle() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplitterCall2 call = reinterpret_cast<CuteQSplitterCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSplitterHandle *>(given);
    }
    return QSplitter::createHandle();
  }

  //  void QSplitter::childEvent(QChildEvent *a0)
  void childEvent(QChildEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSplitterCall3 call = reinterpret_cast<CuteQSplitterCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitter::childEvent(a0);
  }

  //  bool QSplitter::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSplitterCall4 call = reinterpret_cast<CuteQSplitterCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSplitter::event(a0);
  }

  //  void QSplitter::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSplitterCall5 call = reinterpret_cast<CuteQSplitterCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitter::resizeEvent(a0);
  }

  //  void QSplitter::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSplitterCall6 call = reinterpret_cast<CuteQSplitterCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitter::changeEvent(a0);
  }

  //  void QFrame::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSplitterCall7 call = reinterpret_cast<CuteQSplitterCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::paintEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSplitterCall8 call = reinterpret_cast<CuteQSplitterCall8>(taken[8]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSplitterCall9 call = reinterpret_cast<CuteQSplitterCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSplitterCall10 call = reinterpret_cast<CuteQSplitterCall10>(taken[10]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSplitterCall11 call = reinterpret_cast<CuteQSplitterCall11>(taken[11]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSplitterCall12 call = reinterpret_cast<CuteQSplitterCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSplitterCall13 call = reinterpret_cast<CuteQSplitterCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSplitterCall14 call = reinterpret_cast<CuteQSplitterCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSplitterCall15 call = reinterpret_cast<CuteQSplitterCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSplitterCall16 call = reinterpret_cast<CuteQSplitterCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSplitterCall17 call = reinterpret_cast<CuteQSplitterCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSplitterCall18 call = reinterpret_cast<CuteQSplitterCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSplitterCall19 call = reinterpret_cast<CuteQSplitterCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSplitterCall20 call = reinterpret_cast<CuteQSplitterCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSplitterCall21 call = reinterpret_cast<CuteQSplitterCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSplitterCall22 call = reinterpret_cast<CuteQSplitterCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSplitterCall23 call = reinterpret_cast<CuteQSplitterCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSplitterCall24 call = reinterpret_cast<CuteQSplitterCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSplitterCall25 call = reinterpret_cast<CuteQSplitterCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSplitterCall26 call = reinterpret_cast<CuteQSplitterCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSplitterCall27 call = reinterpret_cast<CuteQSplitterCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSplitterCall28 call = reinterpret_cast<CuteQSplitterCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSplitterCall29 call = reinterpret_cast<CuteQSplitterCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSplitterCall30 call = reinterpret_cast<CuteQSplitterCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSplitterCall31 call = reinterpret_cast<CuteQSplitterCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSplitterCall32 call = reinterpret_cast<CuteQSplitterCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSplitterCall33 call = reinterpret_cast<CuteQSplitterCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSplitterCall34 call = reinterpret_cast<CuteQSplitterCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQSplitterCall35 call = reinterpret_cast<CuteQSplitterCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSplitterCall36 call = reinterpret_cast<CuteQSplitterCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQSplitterCall37 call = reinterpret_cast<CuteQSplitterCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSplitterCall38 call = reinterpret_cast<CuteQSplitterCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQSplitterCall39 call = reinterpret_cast<CuteQSplitterCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQSplitterCall40 call = reinterpret_cast<CuteQSplitterCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQSplitterCall41 call = reinterpret_cast<CuteQSplitterCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQSplitterCall42 call = reinterpret_cast<CuteQSplitterCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQSplitterCall43 call = reinterpret_cast<CuteQSplitterCall43>(taken[43]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQSplitterCall44 call = reinterpret_cast<CuteQSplitterCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQSplitterCall45 call = reinterpret_cast<CuteQSplitterCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQSplitterCall46 call = reinterpret_cast<CuteQSplitterCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQSplitterCall47 call = reinterpret_cast<CuteQSplitterCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QSplitter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSplitter10metaObjectEv(
    const QSplitter *self) {
  return self->metaObject();
}

//  QString QSplitter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSplitter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplitter::tr(s, c, n));
}

//  QSplitter::QSplitter(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZN9QSplitterC1EP7QWidget(QWidget *parent) {
  return new CuteQSplitter(parent);
}

//  QSplitter::QSplitter(Qt::Orientation a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZN9QSplitterC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation a0,
    QWidget *parent) {
  return new CuteQSplitter(a0, parent);
}

//  QSplitter::~QSplitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitterD1Ev(QSplitter *self) {
  delete self;
}

//  void QSplitter::addWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter9addWidgetEP7QWidget(
    QSplitter *self,
    QWidget *widget) {
  self->addWidget(widget);
}

//  void QSplitter::insertWidget(int index, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter12insertWidgetEiP7QWidget(
    QSplitter *self,
    int index,
    QWidget *widget) {
  self->insertWidget(index, widget);
}

//  QWidget *QSplitter::replaceWidget(int index, QWidget *widget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN9QSplitter13replaceWidgetEiP7QWidget(
    QSplitter *self,
    int index,
    QWidget *widget) {
  return self->replaceWidget(index, widget);
}

//  void QSplitter::setOrientation(Qt::Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter14setOrientationEN2Qt11OrientationE(
    QSplitter *self,
    Qt::Orientation a0) {
  self->setOrientation(a0);
}

//  Qt::Orientation QSplitter::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK9QSplitter11orientationEv(const QSplitter *self) {
  return self->orientation();
}

//  void QSplitter::setChildrenCollapsible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter22setChildrenCollapsibleEb(
    QSplitter *self,
    bool a0) {
  self->setChildrenCollapsible(a0);
}

//  bool QSplitter::childrenCollapsible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSplitter19childrenCollapsibleEv(const QSplitter *self) {
  return self->childrenCollapsible();
}

//  void QSplitter::setCollapsible(int index, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter14setCollapsibleEib(
    QSplitter *self,
    int index,
    bool a1) {
  self->setCollapsible(index, a1);
}

//  bool QSplitter::isCollapsible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSplitter13isCollapsibleEi(
    const QSplitter *self,
    int index) {
  return self->isCollapsible(index);
}

//  void QSplitter::setOpaqueResize(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter15setOpaqueResizeEb(QSplitter *self, bool opaque) {
  self->setOpaqueResize(opaque);
}

//  bool QSplitter::opaqueResize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSplitter12opaqueResizeEv(const QSplitter *self) {
  return self->opaqueResize();
}

//  void QSplitter::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter7refreshEv(QSplitter *self) {
  self->refresh();
}

//  QSize QSplitter::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QSplitter8sizeHintEv(const QSplitter *self) {
  return new QSize(self->sizeHint());
}

//  QSize QSplitter::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QSplitter15minimumSizeHintEv(const QSplitter *self) {
  return new QSize(self->minimumSizeHint());
}

//  QByteArray QSplitter::saveState() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QSplitter9saveStateEv(const QSplitter *self) {
  return new QByteArray(self->saveState());
}

//  bool QSplitter::restoreState(const QByteArray &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSplitter12restoreStateERK10QByteArray(
    QSplitter *self,
    const QByteArray *state) {
  return self->restoreState(*state);
}

//  int QSplitter::handleWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSplitter11handleWidthEv(const QSplitter *self) {
  return self->handleWidth();
}

//  void QSplitter::setHandleWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter14setHandleWidthEi(QSplitter *self, int a0) {
  self->setHandleWidth(a0);
}

//  int QSplitter::indexOf(QWidget *w) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSplitter7indexOfEP7QWidget(
    const QSplitter *self,
    QWidget *w) {
  return self->indexOf(w);
}

//  QWidget *QSplitter::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK9QSplitter6widgetEi(const QSplitter *self, int index) {
  return self->widget(index);
}

//  int QSplitter::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSplitter5countEv(const QSplitter *self) {
  return self->count();
}

//  void QSplitter::getRange(int index, int *a1, int *a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QSplitter8getRangeEiPiS0_(
    const QSplitter *self,
    int index,
    int *a1,
    int *a2) {
  self->getRange(index, a1, a2);
}

//  QSplitterHandle *QSplitter::handle(int index) const
extern "C" Q_DECL_EXPORT
QSplitterHandle *ritual_ZNK9QSplitter6handleEi(
    const QSplitter *self,
    int index) {
  return self->handle(index);
}

//  void QSplitter::setStretchFactor(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter16setStretchFactorEii(
    QSplitter *self,
    int index,
    int stretch) {
  self->setStretchFactor(index, stretch);
}

//  a Python function taken by a CuteQSplitter, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSplitter(QSplitter *self, const char *key, void *call) {
  return static_cast<CuteQSplitter *>(self)->take(key, call);
}

//  QSize QSplitter::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QSplitter8sizeHintEv(const QSplitter *self) {
  return new QSize(self->QSplitter::sizeHint());
}

//  QSize QSplitter::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QSplitter15minimumSizeHintEv(const QSplitter *self) {
  return new QSize(self->QSplitter::minimumSizeHint());
}

//  QSplitterHandle *QSplitter::createHandle()
extern "C" Q_DECL_EXPORT
QSplitterHandle *ritual_own_ZN9QSplitter12createHandleEv(QSplitter *self) {
  return static_cast<OwnQSplitter *>(self)->OwnQSplitter::createHandle();
}

//  void QSplitter::childEvent(QChildEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSplitter10childEventEP11QChildEvent(
    QSplitter *self,
    QChildEvent *a0) {
  static_cast<OwnQSplitter *>(self)->OwnQSplitter::childEvent(a0);
}

//  bool QSplitter::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QSplitter5eventEP6QEvent(QSplitter *self, QEvent *a0) {
  return static_cast<OwnQSplitter *>(self)->OwnQSplitter::event(a0);
}

//  void QSplitter::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSplitter11resizeEventEP12QResizeEvent(
    QSplitter *self,
    QResizeEvent *a0) {
  static_cast<OwnQSplitter *>(self)->OwnQSplitter::resizeEvent(a0);
}

//  void QSplitter::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSplitter11changeEventEP6QEvent(
    QSplitter *self,
    QEvent *a0) {
  static_cast<OwnQSplitter *>(self)->OwnQSplitter::changeEvent(a0);
}
