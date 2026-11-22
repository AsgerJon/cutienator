//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractslider.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractslider.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAbstractSlider may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractSlider : QAbstractSlider {
  using QAbstractSlider::event;
  using QAbstractSlider::keyPressEvent;
  using QAbstractSlider::timerEvent;
  using QAbstractSlider::wheelEvent;
  using QAbstractSlider::changeEvent;
};

//  A QAbstractSlider that Python can take functions over in. Every QAbstractSlider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAbstractSliderCall0)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractSliderCall1)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractSliderCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAbstractSliderCall3)(const void *, QWheelEvent *, int *);
typedef void (*CuteQAbstractSliderCall4)(const void *, QEvent *, int *);
typedef int (*CuteQAbstractSliderCall5)(const void *, int *);
typedef void (*CuteQAbstractSliderCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQAbstractSliderCall7)(const void *, int *);
typedef const QSize * (*CuteQAbstractSliderCall8)(const void *, int *);
typedef int (*CuteQAbstractSliderCall9)(const void *, int, int *);
typedef bool (*CuteQAbstractSliderCall10)(const void *, int *);
typedef void * (*CuteQAbstractSliderCall11)(const void *, int *);
typedef void (*CuteQAbstractSliderCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractSliderCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractSliderCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractSliderCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractSliderCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractSliderCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractSliderCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractSliderCall19)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAbstractSliderCall20)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractSliderCall21)(const void *, QPaintEvent *, int *);
typedef void (*CuteQAbstractSliderCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAbstractSliderCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQAbstractSliderCall24)(const void *, QCloseEvent *, int *);
typedef void (*CuteQAbstractSliderCall25)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQAbstractSliderCall26)(const void *, QTabletEvent *, int *);
typedef void (*CuteQAbstractSliderCall27)(const void *, QActionEvent *, int *);
typedef void (*CuteQAbstractSliderCall28)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQAbstractSliderCall29)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQAbstractSliderCall30)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQAbstractSliderCall31)(const void *, QDropEvent *, int *);
typedef void (*CuteQAbstractSliderCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQAbstractSliderCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQAbstractSliderCall34)(const void *, int, int *);
typedef void (*CuteQAbstractSliderCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQAbstractSliderCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQAbstractSliderCall37)(const void *, int *);
typedef void (*CuteQAbstractSliderCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQAbstractSliderCall39)(const void *, int, int *);
typedef bool (*CuteQAbstractSliderCall40)(const void *, bool, int *);
typedef bool (*CuteQAbstractSliderCall41)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAbstractSliderCall42)(const void *, QChildEvent *, int *);
typedef void (*CuteQAbstractSliderCall43)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractSliderCall44)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAbstractSliderCall45)(const void *, const QMetaMethod *, int *);
class CuteQAbstractSlider : public QAbstractSlider {
public:
  using QAbstractSlider::QAbstractSlider;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[11] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    return false;
  }

  //  bool QAbstractSlider::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSliderCall0 call = reinterpret_cast<CuteQAbstractSliderCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QAbstractSlider::event(e);
  }

  //  void QAbstractSlider::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSliderCall1 call = reinterpret_cast<CuteQAbstractSliderCall1>(taken[1]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QAbstractSlider::keyPressEvent(ev);
  }

  //  void QAbstractSlider::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSliderCall2 call = reinterpret_cast<CuteQAbstractSliderCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractSlider::timerEvent(a0);
  }

  //  void QAbstractSlider::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSliderCall3 call = reinterpret_cast<CuteQAbstractSliderCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::wheelEvent(e);
  }

  //  void QAbstractSlider::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSliderCall4 call = reinterpret_cast<CuteQAbstractSliderCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::changeEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSliderCall5 call = reinterpret_cast<CuteQAbstractSliderCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSliderCall6 call = reinterpret_cast<CuteQAbstractSliderCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSliderCall7 call = reinterpret_cast<CuteQAbstractSliderCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractSliderCall8 call = reinterpret_cast<CuteQAbstractSliderCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractSliderCall9 call = reinterpret_cast<CuteQAbstractSliderCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractSliderCall10 call = reinterpret_cast<CuteQAbstractSliderCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSliderCall11 call = reinterpret_cast<CuteQAbstractSliderCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSliderCall12 call = reinterpret_cast<CuteQAbstractSliderCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractSliderCall13 call = reinterpret_cast<CuteQAbstractSliderCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractSliderCall14 call = reinterpret_cast<CuteQAbstractSliderCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractSliderCall15 call = reinterpret_cast<CuteQAbstractSliderCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractSliderCall16 call = reinterpret_cast<CuteQAbstractSliderCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractSliderCall17 call = reinterpret_cast<CuteQAbstractSliderCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractSliderCall18 call = reinterpret_cast<CuteQAbstractSliderCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractSliderCall19 call = reinterpret_cast<CuteQAbstractSliderCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractSliderCall20 call = reinterpret_cast<CuteQAbstractSliderCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractSliderCall21 call = reinterpret_cast<CuteQAbstractSliderCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractSliderCall22 call = reinterpret_cast<CuteQAbstractSliderCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractSliderCall23 call = reinterpret_cast<CuteQAbstractSliderCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractSliderCall24 call = reinterpret_cast<CuteQAbstractSliderCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractSliderCall25 call = reinterpret_cast<CuteQAbstractSliderCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractSliderCall26 call = reinterpret_cast<CuteQAbstractSliderCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractSliderCall27 call = reinterpret_cast<CuteQAbstractSliderCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractSliderCall28 call = reinterpret_cast<CuteQAbstractSliderCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractSliderCall29 call = reinterpret_cast<CuteQAbstractSliderCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractSliderCall30 call = reinterpret_cast<CuteQAbstractSliderCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractSliderCall31 call = reinterpret_cast<CuteQAbstractSliderCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractSliderCall32 call = reinterpret_cast<CuteQAbstractSliderCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractSliderCall33 call = reinterpret_cast<CuteQAbstractSliderCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractSliderCall34 call = reinterpret_cast<CuteQAbstractSliderCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractSliderCall35 call = reinterpret_cast<CuteQAbstractSliderCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractSliderCall36 call = reinterpret_cast<CuteQAbstractSliderCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractSliderCall37 call = reinterpret_cast<CuteQAbstractSliderCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractSliderCall38 call = reinterpret_cast<CuteQAbstractSliderCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractSliderCall39 call = reinterpret_cast<CuteQAbstractSliderCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractSliderCall40 call = reinterpret_cast<CuteQAbstractSliderCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractSliderCall41 call = reinterpret_cast<CuteQAbstractSliderCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractSliderCall42 call = reinterpret_cast<CuteQAbstractSliderCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAbstractSliderCall43 call = reinterpret_cast<CuteQAbstractSliderCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQAbstractSliderCall44 call = reinterpret_cast<CuteQAbstractSliderCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQAbstractSliderCall45 call = reinterpret_cast<CuteQAbstractSliderCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QAbstractSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractSlider10metaObjectEv(
    const QAbstractSlider *self) {
  return self->metaObject();
}

//  QString QAbstractSlider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractSlider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSlider::tr(s, c, n));
}

//  QAbstractSlider::QAbstractSlider(QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractSlider *ritual_ZN15QAbstractSliderC1EP7QWidget(QWidget *parent) {
  return new CuteQAbstractSlider(parent);
}

//  QAbstractSlider::~QAbstractSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSliderD1Ev(QAbstractSlider *self) {
  delete self;
}

//  Qt::Orientation QAbstractSlider::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QAbstractSlider11orientationEv(
    const QAbstractSlider *self) {
  return self->orientation();
}

//  void QAbstractSlider::setMinimum(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider10setMinimumEi(
    QAbstractSlider *self,
    int a0) {
  self->setMinimum(a0);
}

//  int QAbstractSlider::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider7minimumEv(const QAbstractSlider *self) {
  return self->minimum();
}

//  void QAbstractSlider::setMaximum(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider10setMaximumEi(
    QAbstractSlider *self,
    int a0) {
  self->setMaximum(a0);
}

//  int QAbstractSlider::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider7maximumEv(const QAbstractSlider *self) {
  return self->maximum();
}

//  void QAbstractSlider::setSingleStep(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider13setSingleStepEi(
    QAbstractSlider *self,
    int a0) {
  self->setSingleStep(a0);
}

//  int QAbstractSlider::singleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider10singleStepEv(const QAbstractSlider *self) {
  return self->singleStep();
}

//  void QAbstractSlider::setPageStep(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider11setPageStepEi(
    QAbstractSlider *self,
    int a0) {
  self->setPageStep(a0);
}

//  int QAbstractSlider::pageStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider8pageStepEv(const QAbstractSlider *self) {
  return self->pageStep();
}

//  void QAbstractSlider::setTracking(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider11setTrackingEb(
    QAbstractSlider *self,
    bool enable) {
  self->setTracking(enable);
}

//  bool QAbstractSlider::hasTracking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider11hasTrackingEv(
    const QAbstractSlider *self) {
  return self->hasTracking();
}

//  void QAbstractSlider::setSliderDown(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider13setSliderDownEb(
    QAbstractSlider *self,
    bool a0) {
  self->setSliderDown(a0);
}

//  bool QAbstractSlider::isSliderDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider12isSliderDownEv(
    const QAbstractSlider *self) {
  return self->isSliderDown();
}

//  void QAbstractSlider::setSliderPosition(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider17setSliderPositionEi(
    QAbstractSlider *self,
    int a0) {
  self->setSliderPosition(a0);
}

//  int QAbstractSlider::sliderPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider14sliderPositionEv(
    const QAbstractSlider *self) {
  return self->sliderPosition();
}

//  void QAbstractSlider::setInvertedAppearance(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider21setInvertedAppearanceEb(
    QAbstractSlider *self,
    bool a0) {
  self->setInvertedAppearance(a0);
}

//  bool QAbstractSlider::invertedAppearance() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider18invertedAppearanceEv(
    const QAbstractSlider *self) {
  return self->invertedAppearance();
}

//  void QAbstractSlider::setInvertedControls(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider19setInvertedControlsEb(
    QAbstractSlider *self,
    bool a0) {
  self->setInvertedControls(a0);
}

//  bool QAbstractSlider::invertedControls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider16invertedControlsEv(
    const QAbstractSlider *self) {
  return self->invertedControls();
}

//  int QAbstractSlider::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider5valueEv(const QAbstractSlider *self) {
  return self->value();
}

//  void QAbstractSlider::triggerAction(SliderAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider13triggerActionENS_12SliderActionE(
    QAbstractSlider *self,
    QAbstractSlider::SliderAction action) {
  self->triggerAction(action);
}

//  void QAbstractSlider::setValue(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider8setValueEi(QAbstractSlider *self, int a0) {
  self->setValue(a0);
}

//  void QAbstractSlider::setOrientation(Qt::Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider14setOrientationEN2Qt11OrientationE(
    QAbstractSlider *self,
    Qt::Orientation a0) {
  self->setOrientation(a0);
}

//  void QAbstractSlider::setRange(int min, int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider8setRangeEii(
    QAbstractSlider *self,
    int min,
    int max) {
  self->setRange(min, max);
}

//  a Python function taken by a CuteQAbstractSlider, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSlider(
    QAbstractSlider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSlider *>(self)->take(key, call);
}

//  bool QAbstractSlider::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSlider5eventEP6QEvent(
    QAbstractSlider *self,
    QEvent *e) {
  return static_cast<OwnQAbstractSlider *>(self)->OwnQAbstractSlider::event(
      e);
}

//  void QAbstractSlider::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSlider13keyPressEventEP9QKeyEvent(
    QAbstractSlider *self,
    QKeyEvent *ev) {
  static_cast<OwnQAbstractSlider *>(self)->OwnQAbstractSlider::keyPressEvent(
      ev);
}

//  void QAbstractSlider::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSlider10timerEventEP11QTimerEvent(
    QAbstractSlider *self,
    QTimerEvent *a0) {
  static_cast<OwnQAbstractSlider *>(self)->OwnQAbstractSlider::timerEvent(
      a0);
}

//  void QAbstractSlider::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSlider10wheelEventEP11QWheelEvent(
    QAbstractSlider *self,
    QWheelEvent *e) {
  static_cast<OwnQAbstractSlider *>(self)->OwnQAbstractSlider::wheelEvent(e);
}

//  void QAbstractSlider::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSlider11changeEventEP6QEvent(
    QAbstractSlider *self,
    QEvent *e) {
  static_cast<OwnQAbstractSlider *>(self)->OwnQAbstractSlider::changeEvent(
      e);
}
