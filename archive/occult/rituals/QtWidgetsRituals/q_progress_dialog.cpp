//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qprogressdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qprogressdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QProgressDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQProgressDialog : QProgressDialog {
  using QProgressDialog::resizeEvent;
  using QProgressDialog::closeEvent;
  using QProgressDialog::changeEvent;
  using QProgressDialog::showEvent;
};

//  A QProgressDialog that Python can take functions over in. Every QProgressDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQProgressDialogCall0)(const void *, int *);
typedef void (*CuteQProgressDialogCall1)(const void *, QResizeEvent *, int *);
typedef void (*CuteQProgressDialogCall2)(const void *, QCloseEvent *, int *);
typedef void (*CuteQProgressDialogCall3)(const void *, QEvent *, int *);
typedef void (*CuteQProgressDialogCall4)(const void *, QShowEvent *, int *);
typedef void (*CuteQProgressDialogCall5)(const void *, bool, int *);
typedef const QSize * (*CuteQProgressDialogCall6)(const void *, int *);
typedef void (*CuteQProgressDialogCall7)(const void *, int *);
typedef int (*CuteQProgressDialogCall8)(const void *, int *);
typedef void (*CuteQProgressDialogCall9)(const void *, int, int *);
typedef void (*CuteQProgressDialogCall10)(const void *, int *);
typedef void (*CuteQProgressDialogCall11)(const void *, int *);
typedef void (*CuteQProgressDialogCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQProgressDialogCall13)(const void *, QContextMenuEvent *, int *);
typedef bool (*CuteQProgressDialogCall14)(const void *, QObject *, QEvent *, int *);
typedef int (*CuteQProgressDialogCall15)(const void *, int *);
typedef int (*CuteQProgressDialogCall16)(const void *, int, int *);
typedef bool (*CuteQProgressDialogCall17)(const void *, int *);
typedef void * (*CuteQProgressDialogCall18)(const void *, int *);
typedef bool (*CuteQProgressDialogCall19)(const void *, QEvent *, int *);
typedef void (*CuteQProgressDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressDialogCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressDialogCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQProgressDialogCall24)(const void *, QWheelEvent *, int *);
typedef void (*CuteQProgressDialogCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQProgressDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQProgressDialogCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQProgressDialogCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQProgressDialogCall29)(const void *, QEvent *, int *);
typedef void (*CuteQProgressDialogCall30)(const void *, QPaintEvent *, int *);
typedef void (*CuteQProgressDialogCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQProgressDialogCall32)(const void *, QTabletEvent *, int *);
typedef void (*CuteQProgressDialogCall33)(const void *, QActionEvent *, int *);
typedef void (*CuteQProgressDialogCall34)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQProgressDialogCall35)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQProgressDialogCall36)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQProgressDialogCall37)(const void *, QDropEvent *, int *);
typedef void (*CuteQProgressDialogCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQProgressDialogCall39)(const void *, int, int *);
typedef void (*CuteQProgressDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQProgressDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQProgressDialogCall42)(const void *, int *);
typedef void (*CuteQProgressDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQProgressDialogCall44)(const void *, int, int *);
typedef bool (*CuteQProgressDialogCall45)(const void *, bool, int *);
typedef void (*CuteQProgressDialogCall46)(const void *, QTimerEvent *, int *);
typedef void (*CuteQProgressDialogCall47)(const void *, QChildEvent *, int *);
typedef void (*CuteQProgressDialogCall48)(const void *, QEvent *, int *);
typedef void (*CuteQProgressDialogCall49)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQProgressDialogCall50)(const void *, const QMetaMethod *, int *);
class CuteQProgressDialog : public QProgressDialog {
public:
  using QProgressDialog::QProgressDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
    return false;
  }

  //  QSize QProgressDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQProgressDialogCall0 call = reinterpret_cast<CuteQProgressDialogCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QProgressDialog::sizeHint();
  }

  //  void QProgressDialog::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProgressDialogCall1 call = reinterpret_cast<CuteQProgressDialogCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QProgressDialog::resizeEvent(event);
  }

  //  void QProgressDialog::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQProgressDialogCall2 call = reinterpret_cast<CuteQProgressDialogCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QProgressDialog::closeEvent(event);
  }

  //  void QProgressDialog::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQProgressDialogCall3 call = reinterpret_cast<CuteQProgressDialogCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QProgressDialog::changeEvent(event);
  }

  //  void QProgressDialog::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQProgressDialogCall4 call = reinterpret_cast<CuteQProgressDialogCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QProgressDialog::showEvent(event);
  }

  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[5]) {
      int handled = 0;
      CuteQProgressDialogCall5 call = reinterpret_cast<CuteQProgressDialogCall5>(taken[5]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }

  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQProgressDialogCall6 call = reinterpret_cast<CuteQProgressDialogCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }

  //  void QDialog::open()
  void open() override {
    if (taken[7]) {
      int handled = 0;
      CuteQProgressDialogCall7 call = reinterpret_cast<CuteQProgressDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }

  //  int QDialog::exec()
  int exec() override {
    if (taken[8]) {
      int handled = 0;
      CuteQProgressDialogCall8 call = reinterpret_cast<CuteQProgressDialogCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }

  //  void QDialog::done(int a0)
  void done(int a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQProgressDialogCall9 call = reinterpret_cast<CuteQProgressDialogCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::done(a0);
  }

  //  void QDialog::accept()
  void accept() override {
    if (taken[10]) {
      int handled = 0;
      CuteQProgressDialogCall10 call = reinterpret_cast<CuteQProgressDialogCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }

  //  void QDialog::reject()
  void reject() override {
    if (taken[11]) {
      int handled = 0;
      CuteQProgressDialogCall11 call = reinterpret_cast<CuteQProgressDialogCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }

  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQProgressDialogCall12 call = reinterpret_cast<CuteQProgressDialogCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }

  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQProgressDialogCall13 call = reinterpret_cast<CuteQProgressDialogCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }

  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQProgressDialogCall14 call = reinterpret_cast<CuteQProgressDialogCall14>(taken[14]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQProgressDialogCall15 call = reinterpret_cast<CuteQProgressDialogCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQProgressDialogCall16 call = reinterpret_cast<CuteQProgressDialogCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQProgressDialogCall17 call = reinterpret_cast<CuteQProgressDialogCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQProgressDialogCall18 call = reinterpret_cast<CuteQProgressDialogCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQProgressDialogCall19 call = reinterpret_cast<CuteQProgressDialogCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQProgressDialogCall20 call = reinterpret_cast<CuteQProgressDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQProgressDialogCall21 call = reinterpret_cast<CuteQProgressDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQProgressDialogCall22 call = reinterpret_cast<CuteQProgressDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQProgressDialogCall23 call = reinterpret_cast<CuteQProgressDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQProgressDialogCall24 call = reinterpret_cast<CuteQProgressDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQProgressDialogCall25 call = reinterpret_cast<CuteQProgressDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQProgressDialogCall26 call = reinterpret_cast<CuteQProgressDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQProgressDialogCall27 call = reinterpret_cast<CuteQProgressDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQProgressDialogCall28 call = reinterpret_cast<CuteQProgressDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQProgressDialogCall29 call = reinterpret_cast<CuteQProgressDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQProgressDialogCall30 call = reinterpret_cast<CuteQProgressDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQProgressDialogCall31 call = reinterpret_cast<CuteQProgressDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQProgressDialogCall32 call = reinterpret_cast<CuteQProgressDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQProgressDialogCall33 call = reinterpret_cast<CuteQProgressDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQProgressDialogCall34 call = reinterpret_cast<CuteQProgressDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQProgressDialogCall35 call = reinterpret_cast<CuteQProgressDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQProgressDialogCall36 call = reinterpret_cast<CuteQProgressDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQProgressDialogCall37 call = reinterpret_cast<CuteQProgressDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQProgressDialogCall38 call = reinterpret_cast<CuteQProgressDialogCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQProgressDialogCall39 call = reinterpret_cast<CuteQProgressDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQProgressDialogCall40 call = reinterpret_cast<CuteQProgressDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQProgressDialogCall41 call = reinterpret_cast<CuteQProgressDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQProgressDialogCall42 call = reinterpret_cast<CuteQProgressDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQProgressDialogCall43 call = reinterpret_cast<CuteQProgressDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQProgressDialogCall44 call = reinterpret_cast<CuteQProgressDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQProgressDialogCall45 call = reinterpret_cast<CuteQProgressDialogCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQProgressDialogCall46 call = reinterpret_cast<CuteQProgressDialogCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQProgressDialogCall47 call = reinterpret_cast<CuteQProgressDialogCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQProgressDialogCall48 call = reinterpret_cast<CuteQProgressDialogCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQProgressDialogCall49 call = reinterpret_cast<CuteQProgressDialogCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQProgressDialogCall50 call = reinterpret_cast<CuteQProgressDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QProgressDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QProgressDialog10metaObjectEv(
    const QProgressDialog *self) {
  return self->metaObject();
}

//  QString QProgressDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QProgressDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProgressDialog::tr(s, c, n));
}

//  QProgressDialog::QProgressDialog(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QProgressDialog *ritual_ZN15QProgressDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQProgressDialog(
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QProgressDialog::QProgressDialog(const QString &labelText, const QString
//      &cancelButtonText, int minimum, int maximum, QWidget *parent,
//      Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QProgressDialog *ritual_ZN15QProgressDialogC1ERK7QStringS2_iiP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *labelText,
    const QString *cancelButtonText,
    int minimum,
    int maximum,
    QWidget *parent,
    int flags) {
  return new CuteQProgressDialog(
      *labelText,
      *cancelButtonText,
      minimum,
      maximum,
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QProgressDialog::~QProgressDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialogD1Ev(QProgressDialog *self) {
  delete self;
}

//  void QProgressDialog::setLabel(QLabel *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog8setLabelEP6QLabel(
    QProgressDialog *self,
    QLabel *label) {
  self->setLabel(label);
}

//  void QProgressDialog::setCancelButton(QPushButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog15setCancelButtonEP11QPushButton(
    QProgressDialog *self,
    QPushButton *button) {
  self->setCancelButton(button);
}

//  void QProgressDialog::setBar(QProgressBar *bar)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog6setBarEP12QProgressBar(
    QProgressDialog *self,
    QProgressBar *bar) {
  self->setBar(bar);
}

//  bool QProgressDialog::wasCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QProgressDialog11wasCanceledEv(
    const QProgressDialog *self) {
  return self->wasCanceled();
}

//  int QProgressDialog::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog7minimumEv(const QProgressDialog *self) {
  return self->minimum();
}

//  int QProgressDialog::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog7maximumEv(const QProgressDialog *self) {
  return self->maximum();
}

//  int QProgressDialog::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog5valueEv(const QProgressDialog *self) {
  return self->value();
}

//  QSize QProgressDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QProgressDialog8sizeHintEv(const QProgressDialog *self) {
  return new QSize(self->sizeHint());
}

//  QString QProgressDialog::labelText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QProgressDialog9labelTextEv(
    const QProgressDialog *self) {
  return new QString(self->labelText());
}

//  int QProgressDialog::minimumDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog15minimumDurationEv(
    const QProgressDialog *self) {
  return self->minimumDuration();
}

//  void QProgressDialog::setAutoReset(bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog12setAutoResetEb(
    QProgressDialog *self,
    bool reset) {
  self->setAutoReset(reset);
}

//  bool QProgressDialog::autoReset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QProgressDialog9autoResetEv(const QProgressDialog *self) {
  return self->autoReset();
}

//  void QProgressDialog::setAutoClose(bool close)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog12setAutoCloseEb(
    QProgressDialog *self,
    bool close) {
  self->setAutoClose(close);
}

//  bool QProgressDialog::autoClose() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QProgressDialog9autoCloseEv(const QProgressDialog *self) {
  return self->autoClose();
}

//  void QProgressDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog4openEP7QObjectPKc(
    QProgressDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QProgressDialog::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog6cancelEv(QProgressDialog *self) {
  self->cancel();
}

//  void QProgressDialog::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog5resetEv(QProgressDialog *self) {
  self->reset();
}

//  void QProgressDialog::setMaximum(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog10setMaximumEi(
    QProgressDialog *self,
    int maximum) {
  self->setMaximum(maximum);
}

//  void QProgressDialog::setMinimum(int minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog10setMinimumEi(
    QProgressDialog *self,
    int minimum) {
  self->setMinimum(minimum);
}

//  void QProgressDialog::setRange(int minimum, int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog8setRangeEii(
    QProgressDialog *self,
    int minimum,
    int maximum) {
  self->setRange(minimum, maximum);
}

//  void QProgressDialog::setValue(int progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog8setValueEi(
    QProgressDialog *self,
    int progress) {
  self->setValue(progress);
}

//  void QProgressDialog::setLabelText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog12setLabelTextERK7QString(
    QProgressDialog *self,
    const QString *text) {
  self->setLabelText(*text);
}

//  void QProgressDialog::setCancelButtonText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog19setCancelButtonTextERK7QString(
    QProgressDialog *self,
    const QString *text) {
  self->setCancelButtonText(*text);
}

//  void QProgressDialog::setMinimumDuration(int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog18setMinimumDurationEi(
    QProgressDialog *self,
    int ms) {
  self->setMinimumDuration(ms);
}

//  void QProgressDialog::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog11resizeEventEP12QResizeEvent(
    QProgressDialog *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QProgressDialog::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog10closeEventEP11QCloseEvent(
    QProgressDialog *self,
    QCloseEvent *event) {
  self->closeEvent(event);
}

//  void QProgressDialog::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog11changeEventEP6QEvent(
    QProgressDialog *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QProgressDialog::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog9showEventEP10QShowEvent(
    QProgressDialog *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QProgressDialog::forceShow()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog9forceShowEv(QProgressDialog *self) {
  self->forceShow();
}

//  a Python function taken by a CuteQProgressDialog, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProgressDialog(
    QProgressDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProgressDialog *>(self)->take(key, call);
}

//  QSize QProgressDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QProgressDialog8sizeHintEv(
    const QProgressDialog *self) {
  return new QSize(self->QProgressDialog::sizeHint());
}

//  void QProgressDialog::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QProgressDialog11resizeEventEP12QResizeEvent(
    QProgressDialog *self,
    QResizeEvent *event) {
  static_cast<OwnQProgressDialog *>(self)->OwnQProgressDialog::resizeEvent(
      event);
}

//  void QProgressDialog::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QProgressDialog10closeEventEP11QCloseEvent(
    QProgressDialog *self,
    QCloseEvent *event) {
  static_cast<OwnQProgressDialog *>(self)->OwnQProgressDialog::closeEvent(
      event);
}

//  void QProgressDialog::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QProgressDialog11changeEventEP6QEvent(
    QProgressDialog *self,
    QEvent *event) {
  static_cast<OwnQProgressDialog *>(self)->OwnQProgressDialog::changeEvent(
      event);
}

//  void QProgressDialog::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QProgressDialog9showEventEP10QShowEvent(
    QProgressDialog *self,
    QShowEvent *event) {
  static_cast<OwnQProgressDialog *>(self)->OwnQProgressDialog::showEvent(
      event);
}
