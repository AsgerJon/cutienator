//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcombobox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcombobox.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtGui/qicon.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QComboBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQComboBox : QComboBox {
  using QComboBox::focusInEvent;
  using QComboBox::focusOutEvent;
  using QComboBox::changeEvent;
  using QComboBox::resizeEvent;
  using QComboBox::paintEvent;
  using QComboBox::showEvent;
  using QComboBox::hideEvent;
  using QComboBox::mousePressEvent;
  using QComboBox::mouseReleaseEvent;
  using QComboBox::keyPressEvent;
  using QComboBox::keyReleaseEvent;
  using QComboBox::wheelEvent;
  using QComboBox::contextMenuEvent;
  using QComboBox::inputMethodEvent;
  using QComboBox::initStyleOption;
};

//  A QComboBox that Python can take functions over in. Every QComboBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQComboBoxCall0)(const void *, QAbstractItemModel *, int *);
typedef const QSize * (*CuteQComboBoxCall1)(const void *, int *);
typedef const QSize * (*CuteQComboBoxCall2)(const void *, int *);
typedef void (*CuteQComboBoxCall3)(const void *, int *);
typedef void (*CuteQComboBoxCall4)(const void *, int *);
typedef bool (*CuteQComboBoxCall5)(const void *, QEvent *, int *);
typedef const QVariant * (*CuteQComboBoxCall6)(const void *, int, int *);
typedef void (*CuteQComboBoxCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQComboBoxCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQComboBoxCall9)(const void *, QEvent *, int *);
typedef void (*CuteQComboBoxCall10)(const void *, QResizeEvent *, int *);
typedef void (*CuteQComboBoxCall11)(const void *, QPaintEvent *, int *);
typedef void (*CuteQComboBoxCall12)(const void *, QShowEvent *, int *);
typedef void (*CuteQComboBoxCall13)(const void *, QHideEvent *, int *);
typedef void (*CuteQComboBoxCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxCall18)(const void *, QWheelEvent *, int *);
typedef void (*CuteQComboBoxCall19)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQComboBoxCall20)(const void *, QInputMethodEvent *, int *);
typedef void (*CuteQComboBoxCall21)(const void *, QStyleOptionComboBox *, int *);
typedef int (*CuteQComboBoxCall22)(const void *, int *);
typedef void (*CuteQComboBoxCall23)(const void *, bool, int *);
typedef int (*CuteQComboBoxCall24)(const void *, int, int *);
typedef bool (*CuteQComboBoxCall25)(const void *, int *);
typedef void * (*CuteQComboBoxCall26)(const void *, int *);
typedef void (*CuteQComboBoxCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQComboBoxCall30)(const void *, QEvent *, int *);
typedef void (*CuteQComboBoxCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQComboBoxCall32)(const void *, QCloseEvent *, int *);
typedef void (*CuteQComboBoxCall33)(const void *, QTabletEvent *, int *);
typedef void (*CuteQComboBoxCall34)(const void *, QActionEvent *, int *);
typedef void (*CuteQComboBoxCall35)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQComboBoxCall36)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQComboBoxCall37)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQComboBoxCall38)(const void *, QDropEvent *, int *);
typedef int (*CuteQComboBoxCall39)(const void *, int, int *);
typedef void (*CuteQComboBoxCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQComboBoxCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQComboBoxCall42)(const void *, int *);
typedef bool (*CuteQComboBoxCall43)(const void *, bool, int *);
typedef bool (*CuteQComboBoxCall44)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQComboBoxCall45)(const void *, QTimerEvent *, int *);
typedef void (*CuteQComboBoxCall46)(const void *, QChildEvent *, int *);
typedef void (*CuteQComboBoxCall47)(const void *, QEvent *, int *);
typedef void (*CuteQComboBoxCall48)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQComboBoxCall49)(const void *, const QMetaMethod *, int *);
class CuteQComboBox : public QComboBox {
public:
  using QComboBox::QComboBox;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QComboBox8setModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QComboBox9showPopupEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QComboBox9hidePopupEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QComboBox15initStyleOptionEP20QStyleOptionComboBox")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    return false;
  }

  //  void QComboBox::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboBoxCall0 call = reinterpret_cast<CuteQComboBoxCall0>(taken[0]);
      call(this, model, &handled);
      if (handled) return;
    }
    QComboBox::setModel(model);
  }

  //  QSize QComboBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboBoxCall1 call = reinterpret_cast<CuteQComboBoxCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QComboBox::sizeHint();
  }

  //  QSize QComboBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQComboBoxCall2 call = reinterpret_cast<CuteQComboBoxCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QComboBox::minimumSizeHint();
  }

  //  void QComboBox::showPopup()
  void showPopup() override {
    if (taken[3]) {
      int handled = 0;
      CuteQComboBoxCall3 call = reinterpret_cast<CuteQComboBoxCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QComboBox::showPopup();
  }

  //  void QComboBox::hidePopup()
  void hidePopup() override {
    if (taken[4]) {
      int handled = 0;
      CuteQComboBoxCall4 call = reinterpret_cast<CuteQComboBoxCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QComboBox::hidePopup();
  }

  //  bool QComboBox::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQComboBoxCall5 call = reinterpret_cast<CuteQComboBoxCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QComboBox::event(event);
  }

  //  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQComboBoxCall6 call = reinterpret_cast<CuteQComboBoxCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QComboBox::inputMethodQuery(a0);
  }

  //  void QComboBox::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQComboBoxCall7 call = reinterpret_cast<CuteQComboBoxCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::focusInEvent(e);
  }

  //  void QComboBox::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQComboBoxCall8 call = reinterpret_cast<CuteQComboBoxCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::focusOutEvent(e);
  }

  //  void QComboBox::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQComboBoxCall9 call = reinterpret_cast<CuteQComboBoxCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::changeEvent(e);
  }

  //  void QComboBox::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQComboBoxCall10 call = reinterpret_cast<CuteQComboBoxCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::resizeEvent(e);
  }

  //  void QComboBox::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQComboBoxCall11 call = reinterpret_cast<CuteQComboBoxCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::paintEvent(e);
  }

  //  void QComboBox::showEvent(QShowEvent *e)
  void showEvent(QShowEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQComboBoxCall12 call = reinterpret_cast<CuteQComboBoxCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::showEvent(e);
  }

  //  void QComboBox::hideEvent(QHideEvent *e)
  void hideEvent(QHideEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQComboBoxCall13 call = reinterpret_cast<CuteQComboBoxCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::hideEvent(e);
  }

  //  void QComboBox::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQComboBoxCall14 call = reinterpret_cast<CuteQComboBoxCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::mousePressEvent(e);
  }

  //  void QComboBox::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQComboBoxCall15 call = reinterpret_cast<CuteQComboBoxCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::mouseReleaseEvent(e);
  }

  //  void QComboBox::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQComboBoxCall16 call = reinterpret_cast<CuteQComboBoxCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::keyPressEvent(e);
  }

  //  void QComboBox::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQComboBoxCall17 call = reinterpret_cast<CuteQComboBoxCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::keyReleaseEvent(e);
  }

  //  void QComboBox::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQComboBoxCall18 call = reinterpret_cast<CuteQComboBoxCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::wheelEvent(e);
  }

  //  void QComboBox::contextMenuEvent(QContextMenuEvent *e)
  void contextMenuEvent(QContextMenuEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQComboBoxCall19 call = reinterpret_cast<CuteQComboBoxCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::contextMenuEvent(e);
  }

  //  void QComboBox::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQComboBoxCall20 call = reinterpret_cast<CuteQComboBoxCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QComboBox::inputMethodEvent(a0);
  }

  //  void QComboBox::initStyleOption(QStyleOptionComboBox *option) const
  void initStyleOption(QStyleOptionComboBox *option) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQComboBoxCall21 call = reinterpret_cast<CuteQComboBoxCall21>(taken[21]);
      call(this, option, &handled);
      if (handled) return;
    }
    QComboBox::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQComboBoxCall22 call = reinterpret_cast<CuteQComboBoxCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[23]) {
      int handled = 0;
      CuteQComboBoxCall23 call = reinterpret_cast<CuteQComboBoxCall23>(taken[23]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQComboBoxCall24 call = reinterpret_cast<CuteQComboBoxCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQComboBoxCall25 call = reinterpret_cast<CuteQComboBoxCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQComboBoxCall26 call = reinterpret_cast<CuteQComboBoxCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQComboBoxCall27 call = reinterpret_cast<CuteQComboBoxCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQComboBoxCall28 call = reinterpret_cast<CuteQComboBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQComboBoxCall29 call = reinterpret_cast<CuteQComboBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQComboBoxCall30 call = reinterpret_cast<CuteQComboBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQComboBoxCall31 call = reinterpret_cast<CuteQComboBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQComboBoxCall32 call = reinterpret_cast<CuteQComboBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQComboBoxCall33 call = reinterpret_cast<CuteQComboBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQComboBoxCall34 call = reinterpret_cast<CuteQComboBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQComboBoxCall35 call = reinterpret_cast<CuteQComboBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQComboBoxCall36 call = reinterpret_cast<CuteQComboBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQComboBoxCall37 call = reinterpret_cast<CuteQComboBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQComboBoxCall38 call = reinterpret_cast<CuteQComboBoxCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQComboBoxCall39 call = reinterpret_cast<CuteQComboBoxCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQComboBoxCall40 call = reinterpret_cast<CuteQComboBoxCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQComboBoxCall41 call = reinterpret_cast<CuteQComboBoxCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQComboBoxCall42 call = reinterpret_cast<CuteQComboBoxCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      CuteQComboBoxCall43 call = reinterpret_cast<CuteQComboBoxCall43>(taken[43]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQComboBoxCall44 call = reinterpret_cast<CuteQComboBoxCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQComboBoxCall45 call = reinterpret_cast<CuteQComboBoxCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQComboBoxCall46 call = reinterpret_cast<CuteQComboBoxCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQComboBoxCall47 call = reinterpret_cast<CuteQComboBoxCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQComboBoxCall48 call = reinterpret_cast<CuteQComboBoxCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQComboBoxCall49 call = reinterpret_cast<CuteQComboBoxCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QComboBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QComboBox10metaObjectEv(
    const QComboBox *self) {
  return self->metaObject();
}

//  QString QComboBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QComboBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QComboBox::tr(s, c, n));
}

//  QComboBox::QComboBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QComboBox *ritual_ZN9QComboBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQComboBox(parent);
}

//  QComboBox::~QComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBoxD1Ev(QComboBox *self) {
  delete self;
}

//  int QComboBox::maxVisibleItems() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox15maxVisibleItemsEv(const QComboBox *self) {
  return self->maxVisibleItems();
}

//  void QComboBox::setMaxVisibleItems(int maxItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox18setMaxVisibleItemsEi(
    QComboBox *self,
    int maxItems) {
  self->setMaxVisibleItems(maxItems);
}

//  int QComboBox::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox5countEv(const QComboBox *self) {
  return self->count();
}

//  void QComboBox::setMaxCount(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setMaxCountEi(QComboBox *self, int max) {
  self->setMaxCount(max);
}

//  int QComboBox::maxCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox8maxCountEv(const QComboBox *self) {
  return self->maxCount();
}

//  bool QComboBox::duplicatesEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QComboBox17duplicatesEnabledEv(const QComboBox *self) {
  return self->duplicatesEnabled();
}

//  void QComboBox::setDuplicatesEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox20setDuplicatesEnabledEb(
    QComboBox *self,
    bool enable) {
  self->setDuplicatesEnabled(enable);
}

//  void QComboBox::setFrame(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox8setFrameEb(QComboBox *self, bool a0) {
  self->setFrame(a0);
}

//  bool QComboBox::hasFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QComboBox8hasFrameEv(const QComboBox *self) {
  return self->hasFrame();
}

//  int QComboBox::findText(const QString &text, Qt::MatchFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox8findTextERK7QString6QFlagsIN2Qt9MatchFlagEE(
    const QComboBox *self,
    const QString *text,
    int flags) {
  return self->findText(*text, QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  int QComboBox::findData(const QVariant &data, int role, Qt::MatchFlags
//      flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox8findDataERK8QVarianti6QFlagsIN2Qt9MatchFlagEE(
    const QComboBox *self,
    const QVariant *data,
    int role,
    int flags) {
  return self->findData(*data, role, QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  InsertPolicy QComboBox::insertPolicy() const
extern "C" Q_DECL_EXPORT
QComboBox::InsertPolicy ritual_ZNK9QComboBox12insertPolicyEv(
    const QComboBox *self) {
  return self->insertPolicy();
}

//  void QComboBox::setInsertPolicy(InsertPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15setInsertPolicyENS_12InsertPolicyE(
    QComboBox *self,
    QComboBox::InsertPolicy policy) {
  self->setInsertPolicy(policy);
}

//  SizeAdjustPolicy QComboBox::sizeAdjustPolicy() const
extern "C" Q_DECL_EXPORT
QComboBox::SizeAdjustPolicy ritual_ZNK9QComboBox16sizeAdjustPolicyEv(
    const QComboBox *self) {
  return self->sizeAdjustPolicy();
}

//  void QComboBox::setSizeAdjustPolicy(SizeAdjustPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox19setSizeAdjustPolicyENS_16SizeAdjustPolicyE(
    QComboBox *self,
    QComboBox::SizeAdjustPolicy policy) {
  self->setSizeAdjustPolicy(policy);
}

//  int QComboBox::minimumContentsLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox21minimumContentsLengthEv(const QComboBox *self) {
  return self->minimumContentsLength();
}

//  void QComboBox::setMinimumContentsLength(int characters)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox24setMinimumContentsLengthEi(
    QComboBox *self,
    int characters) {
  self->setMinimumContentsLength(characters);
}

//  QSize QComboBox::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QComboBox8iconSizeEv(const QComboBox *self) {
  return new QSize(self->iconSize());
}

//  void QComboBox::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setIconSizeERK5QSize(
    QComboBox *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  void QComboBox::setPlaceholderText(const QString &placeholderText)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox18setPlaceholderTextERK7QString(
    QComboBox *self,
    const QString *placeholderText) {
  self->setPlaceholderText(*placeholderText);
}

//  QString QComboBox::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QComboBox15placeholderTextEv(const QComboBox *self) {
  return new QString(self->placeholderText());
}

//  bool QComboBox::isEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QComboBox10isEditableEv(const QComboBox *self) {
  return self->isEditable();
}

//  void QComboBox::setEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setEditableEb(QComboBox *self, bool editable) {
  self->setEditable(editable);
}

//  void QComboBox::setLineEdit(QLineEdit *edit)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setLineEditEP9QLineEdit(
    QComboBox *self,
    QLineEdit *edit) {
  self->setLineEdit(edit);
}

//  QLineEdit *QComboBox::lineEdit() const
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZNK9QComboBox8lineEditEv(const QComboBox *self) {
  return self->lineEdit();
}

//  void QComboBox::setValidator(const QValidator *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox12setValidatorEPK10QValidator(
    QComboBox *self,
    const QValidator *v) {
  self->setValidator(v);
}

//  const QValidator *QComboBox::validator() const
extern "C" Q_DECL_EXPORT
const QValidator *ritual_ZNK9QComboBox9validatorEv(const QComboBox *self) {
  return self->validator();
}

//  void QComboBox::setCompleter(QCompleter *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox12setCompleterEP10QCompleter(
    QComboBox *self,
    QCompleter *c) {
  self->setCompleter(c);
}

//  QCompleter *QComboBox::completer() const
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZNK9QComboBox9completerEv(const QComboBox *self) {
  return self->completer();
}

//  QAbstractItemDelegate *QComboBox::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK9QComboBox12itemDelegateEv(
    const QComboBox *self) {
  return self->itemDelegate();
}

//  void QComboBox::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15setItemDelegateEP21QAbstractItemDelegate(
    QComboBox *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemModel *QComboBox::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK9QComboBox5modelEv(const QComboBox *self) {
  return self->model();
}

//  void QComboBox::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox8setModelEP18QAbstractItemModel(
    QComboBox *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QModelIndex QComboBox::rootModelIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QComboBox14rootModelIndexEv(const QComboBox *self) {
  return new QModelIndex(self->rootModelIndex());
}

//  void QComboBox::setRootModelIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox17setRootModelIndexERK11QModelIndex(
    QComboBox *self,
    const QModelIndex *index) {
  self->setRootModelIndex(*index);
}

//  int QComboBox::modelColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox11modelColumnEv(const QComboBox *self) {
  return self->modelColumn();
}

//  void QComboBox::setModelColumn(int visibleColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox14setModelColumnEi(
    QComboBox *self,
    int visibleColumn) {
  self->setModelColumn(visibleColumn);
}

//  LabelDrawingMode QComboBox::labelDrawingMode() const
extern "C" Q_DECL_EXPORT
QComboBox::LabelDrawingMode ritual_ZNK9QComboBox16labelDrawingModeEv(
    const QComboBox *self) {
  return self->labelDrawingMode();
}

//  void QComboBox::setLabelDrawingMode(LabelDrawingMode labelDrawing)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox19setLabelDrawingModeENS_16LabelDrawingModeE(
    QComboBox *self,
    QComboBox::LabelDrawingMode labelDrawing) {
  self->setLabelDrawingMode(labelDrawing);
}

//  int QComboBox::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox12currentIndexEv(const QComboBox *self) {
  return self->currentIndex();
}

//  QString QComboBox::currentText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QComboBox11currentTextEv(const QComboBox *self) {
  return new QString(self->currentText());
}

//  QVariant QComboBox::currentData(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox11currentDataEi(
    const QComboBox *self,
    int role) {
  return new QVariant(self->currentData(role));
}

//  QString QComboBox::itemText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QComboBox8itemTextEi(const QComboBox *self, int index) {
  return new QString(self->itemText(index));
}

//  QIcon QComboBox::itemIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK9QComboBox8itemIconEi(const QComboBox *self, int index) {
  return new QIcon(self->itemIcon(index));
}

//  QVariant QComboBox::itemData(int index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox8itemDataEii(
    const QComboBox *self,
    int index,
    int role) {
  return new QVariant(self->itemData(index, role));
}

//  void QComboBox::addItem(const QString &text, const QVariant &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox7addItemERK7QStringRK8QVariant(
    QComboBox *self,
    const QString *text,
    const QVariant *userData) {
  self->addItem(*text, *userData);
}

//  void QComboBox::addItem(const QIcon &icon, const QString &text, const
//      QVariant &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox7addItemERK5QIconRK7QStringRK8QVariant(
    QComboBox *self,
    const QIcon *icon,
    const QString *text,
    const QVariant *userData) {
  self->addItem(*icon, *text, *userData);
}

//  void QComboBox::addItems(const QStringList &texts)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox8addItemsERK5QListI7QStringE(
    QComboBox *self,
    const QList<QString> *texts) {
  self->addItems(*texts);
}

//  void QComboBox::insertItem(int index, const QString &text, const QVariant
//      &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10insertItemEiRK7QStringRK8QVariant(
    QComboBox *self,
    int index,
    const QString *text,
    const QVariant *userData) {
  self->insertItem(index, *text, *userData);
}

//  void QComboBox::insertItem(int index, const QIcon &icon, const QString
//      &text, const QVariant &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10insertItemEiRK5QIconRK7QStringRK8QVariant(
    QComboBox *self,
    int index,
    const QIcon *icon,
    const QString *text,
    const QVariant *userData) {
  self->insertItem(index, *icon, *text, *userData);
}

//  void QComboBox::insertItems(int index, const QStringList &texts)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11insertItemsEiRK5QListI7QStringE(
    QComboBox *self,
    int index,
    const QList<QString> *texts) {
  self->insertItems(index, *texts);
}

//  void QComboBox::insertSeparator(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15insertSeparatorEi(QComboBox *self, int index) {
  self->insertSeparator(index);
}

//  void QComboBox::removeItem(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10removeItemEi(QComboBox *self, int index) {
  self->removeItem(index);
}

//  void QComboBox::setItemText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setItemTextEiRK7QString(
    QComboBox *self,
    int index,
    const QString *text) {
  self->setItemText(index, *text);
}

//  void QComboBox::setItemIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setItemIconEiRK5QIcon(
    QComboBox *self,
    int index,
    const QIcon *icon) {
  self->setItemIcon(index, *icon);
}

//  void QComboBox::setItemData(int index, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setItemDataEiRK8QVarianti(
    QComboBox *self,
    int index,
    const QVariant *value,
    int role) {
  self->setItemData(index, *value, role);
}

//  QAbstractItemView *QComboBox::view() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK9QComboBox4viewEv(const QComboBox *self) {
  return self->view();
}

//  void QComboBox::setView(QAbstractItemView *itemView)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox7setViewEP17QAbstractItemView(
    QComboBox *self,
    QAbstractItemView *itemView) {
  self->setView(itemView);
}

//  QSize QComboBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QComboBox8sizeHintEv(const QComboBox *self) {
  return new QSize(self->sizeHint());
}

//  QSize QComboBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QComboBox15minimumSizeHintEv(const QComboBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QComboBox::showPopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox9showPopupEv(QComboBox *self) {
  self->showPopup();
}

//  void QComboBox::hidePopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox9hidePopupEv(QComboBox *self) {
  self->hidePopup();
}

//  bool QComboBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QComboBox5eventEP6QEvent(QComboBox *self, QEvent *event) {
  return self->event(event);
}

//  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QComboBox *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery query, const
//      QVariant &argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryERK8QVariant(
    const QComboBox *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}

//  void QComboBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox5clearEv(QComboBox *self) {
  self->clear();
}

//  void QComboBox::clearEditText()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox13clearEditTextEv(QComboBox *self) {
  self->clearEditText();
}

//  void QComboBox::setEditText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setEditTextERK7QString(
    QComboBox *self,
    const QString *text) {
  self->setEditText(*text);
}

//  void QComboBox::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15setCurrentIndexEi(QComboBox *self, int index) {
  self->setCurrentIndex(index);
}

//  void QComboBox::setCurrentText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox14setCurrentTextERK7QString(
    QComboBox *self,
    const QString *text) {
  self->setCurrentText(*text);
}

//  void QComboBox::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox12focusInEventEP11QFocusEvent(
    QComboBox *self,
    QFocusEvent *e) {
  self->focusInEvent(e);
}

//  void QComboBox::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox13focusOutEventEP11QFocusEvent(
    QComboBox *self,
    QFocusEvent *e) {
  self->focusOutEvent(e);
}

//  void QComboBox::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11changeEventEP6QEvent(QComboBox *self, QEvent *e) {
  self->changeEvent(e);
}

//  void QComboBox::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11resizeEventEP12QResizeEvent(
    QComboBox *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  void QComboBox::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10paintEventEP11QPaintEvent(
    QComboBox *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QComboBox::showEvent(QShowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox9showEventEP10QShowEvent(
    QComboBox *self,
    QShowEvent *e) {
  self->showEvent(e);
}

//  void QComboBox::hideEvent(QHideEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox9hideEventEP10QHideEvent(
    QComboBox *self,
    QHideEvent *e) {
  self->hideEvent(e);
}

//  void QComboBox::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15mousePressEventEP11QMouseEvent(
    QComboBox *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QComboBox::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox17mouseReleaseEventEP11QMouseEvent(
    QComboBox *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

//  void QComboBox::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox13keyPressEventEP9QKeyEvent(
    QComboBox *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  void QComboBox::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15keyReleaseEventEP9QKeyEvent(
    QComboBox *self,
    QKeyEvent *e) {
  self->keyReleaseEvent(e);
}

//  void QComboBox::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10wheelEventEP11QWheelEvent(
    QComboBox *self,
    QWheelEvent *e) {
  self->wheelEvent(e);
}

//  void QComboBox::contextMenuEvent(QContextMenuEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox16contextMenuEventEP17QContextMenuEvent(
    QComboBox *self,
    QContextMenuEvent *e) {
  self->contextMenuEvent(e);
}

//  void QComboBox::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox16inputMethodEventEP17QInputMethodEvent(
    QComboBox *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}

//  void QComboBox::initStyleOption(QStyleOptionComboBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QComboBox15initStyleOptionEP20QStyleOptionComboBox(
    const QComboBox *self,
    QStyleOptionComboBox *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQComboBox, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboBox(QComboBox *self, const char *key, void *call) {
  return static_cast<CuteQComboBox *>(self)->take(key, call);
}

//  void QComboBox::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox8setModelEP18QAbstractItemModel(
    QComboBox *self,
    QAbstractItemModel *model) {
  self->QComboBox::setModel(model);
}

//  QSize QComboBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QComboBox8sizeHintEv(const QComboBox *self) {
  return new QSize(self->QComboBox::sizeHint());
}

//  QSize QComboBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QComboBox15minimumSizeHintEv(const QComboBox *self) {
  return new QSize(self->QComboBox::minimumSizeHint());
}

//  void QComboBox::showPopup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox9showPopupEv(QComboBox *self) {
  self->QComboBox::showPopup();
}

//  void QComboBox::hidePopup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox9hidePopupEv(QComboBox *self) {
  self->QComboBox::hidePopup();
}

//  bool QComboBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QComboBox5eventEP6QEvent(QComboBox *self, QEvent *event) {
  return self->QComboBox::event(event);
}

//  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QComboBox *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->QComboBox::inputMethodQuery(a0));
}

//  void QComboBox::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox12focusInEventEP11QFocusEvent(
    QComboBox *self,
    QFocusEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::focusInEvent(e);
}

//  void QComboBox::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox13focusOutEventEP11QFocusEvent(
    QComboBox *self,
    QFocusEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::focusOutEvent(e);
}

//  void QComboBox::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox11changeEventEP6QEvent(
    QComboBox *self,
    QEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::changeEvent(e);
}

//  void QComboBox::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox11resizeEventEP12QResizeEvent(
    QComboBox *self,
    QResizeEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::resizeEvent(e);
}

//  void QComboBox::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox10paintEventEP11QPaintEvent(
    QComboBox *self,
    QPaintEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::paintEvent(e);
}

//  void QComboBox::showEvent(QShowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox9showEventEP10QShowEvent(
    QComboBox *self,
    QShowEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::showEvent(e);
}

//  void QComboBox::hideEvent(QHideEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox9hideEventEP10QHideEvent(
    QComboBox *self,
    QHideEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::hideEvent(e);
}

//  void QComboBox::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox15mousePressEventEP11QMouseEvent(
    QComboBox *self,
    QMouseEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::mousePressEvent(e);
}

//  void QComboBox::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox17mouseReleaseEventEP11QMouseEvent(
    QComboBox *self,
    QMouseEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::mouseReleaseEvent(e);
}

//  void QComboBox::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox13keyPressEventEP9QKeyEvent(
    QComboBox *self,
    QKeyEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::keyPressEvent(e);
}

//  void QComboBox::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox15keyReleaseEventEP9QKeyEvent(
    QComboBox *self,
    QKeyEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::keyReleaseEvent(e);
}

//  void QComboBox::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox10wheelEventEP11QWheelEvent(
    QComboBox *self,
    QWheelEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::wheelEvent(e);
}

//  void QComboBox::contextMenuEvent(QContextMenuEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox16contextMenuEventEP17QContextMenuEvent(
    QComboBox *self,
    QContextMenuEvent *e) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::contextMenuEvent(e);
}

//  void QComboBox::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QComboBox16inputMethodEventEP17QInputMethodEvent(
    QComboBox *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQComboBox *>(self)->OwnQComboBox::inputMethodEvent(a0);
}

//  void QComboBox::initStyleOption(QStyleOptionComboBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QComboBox15initStyleOptionEP20QStyleOptionComboBox(
    const QComboBox *self,
    QStyleOptionComboBox *option) {
  static_cast<const OwnQComboBox *>(self)->OwnQComboBox::initStyleOption(
      option);
}
