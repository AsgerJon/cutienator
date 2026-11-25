//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxselect.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours. Its Cute
//  class takes over what that of QDialog does: it declares no such function
//  of its own. Nothing it declares is left out.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxselect.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAxSelect that Python can take functions over in. Every QAxSelect
//  Python makes is one. Each function below asks the Python function handed
//  over for it, and runs Qt's own without one.
typedef void (*CuteQAxSelectCall0)(const void *, bool, int *);
typedef const QSize * (*CuteQAxSelectCall1)(const void *, int *);
typedef const QSize * (*CuteQAxSelectCall2)(const void *, int *);
typedef void (*CuteQAxSelectCall3)(const void *, int *);
typedef int (*CuteQAxSelectCall4)(const void *, int *);
typedef void (*CuteQAxSelectCall5)(const void *, int, int *);
typedef void (*CuteQAxSelectCall6)(const void *, int *);
typedef void (*CuteQAxSelectCall7)(const void *, int *);
typedef void (*CuteQAxSelectCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAxSelectCall9)(const void *, QCloseEvent *, int *);
typedef void (*CuteQAxSelectCall10)(const void *, QShowEvent *, int *);
typedef void (*CuteQAxSelectCall11)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQAxSelectCall12)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxSelectCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQAxSelectCall14)(const void *, int *);
typedef int (*CuteQAxSelectCall15)(const void *, int, int *);
typedef bool (*CuteQAxSelectCall16)(const void *, int *);
typedef void * (*CuteQAxSelectCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxSelectCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxSelectCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAxSelectCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAxSelectCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAxSelectCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQAxSelectCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQAxSelectCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAxSelectCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAxSelectCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAxSelectCall27)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAxSelectCall28)(const void *, QEvent *, int *);
typedef void (*CuteQAxSelectCall29)(const void *, QPaintEvent *, int *);
typedef void (*CuteQAxSelectCall30)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAxSelectCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQAxSelectCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAxSelectCall33)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQAxSelectCall34)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQAxSelectCall35)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQAxSelectCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQAxSelectCall37)(const void *, QHideEvent *, int *);
typedef void (*CuteQAxSelectCall38)(const void *, QEvent *, int *);
typedef int (*CuteQAxSelectCall39)(const void *, int, int *);
typedef void (*CuteQAxSelectCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQAxSelectCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQAxSelectCall42)(const void *, int *);
typedef void (*CuteQAxSelectCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQAxSelectCall44)(const void *, int, int *);
typedef bool (*CuteQAxSelectCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxSelectCall46)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAxSelectCall47)(const void *, QChildEvent *, int *);
typedef void (*CuteQAxSelectCall48)(const void *, QEvent *, int *);
typedef void (*CuteQAxSelectCall49)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAxSelectCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxSelect : public QAxSelect {
public:
  using QAxSelect::QAxSelect;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
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
#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxSelectCall0 call = reinterpret_cast<CuteQAxSelectCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }

  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxSelectCall1 call = reinterpret_cast<CuteQAxSelectCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }

  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxSelectCall2 call = reinterpret_cast<CuteQAxSelectCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }

  //  void QDialog::open()
  void open() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxSelectCall3 call = reinterpret_cast<CuteQAxSelectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }

  //  int QDialog::exec()
  int exec() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxSelectCall4 call = reinterpret_cast<CuteQAxSelectCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }

  //  void QDialog::done(int a0)
  void done(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxSelectCall5 call = reinterpret_cast<CuteQAxSelectCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::done(a0);
  }

  //  void QDialog::accept()
  void accept() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxSelectCall6 call = reinterpret_cast<CuteQAxSelectCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }

  //  void QDialog::reject()
  void reject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAxSelectCall7 call = reinterpret_cast<CuteQAxSelectCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }

  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAxSelectCall8 call = reinterpret_cast<CuteQAxSelectCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }

  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAxSelectCall9 call = reinterpret_cast<CuteQAxSelectCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }

  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAxSelectCall10 call = reinterpret_cast<CuteQAxSelectCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }

  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAxSelectCall11 call = reinterpret_cast<CuteQAxSelectCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::resizeEvent(a0);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAxSelectCall12 call = reinterpret_cast<CuteQAxSelectCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if !defined(QT_NO_QOBJECT)
  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAxSelectCall13 call = reinterpret_cast<CuteQAxSelectCall13>(taken[13]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAxSelectCall14 call = reinterpret_cast<CuteQAxSelectCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAxSelectCall15 call = reinterpret_cast<CuteQAxSelectCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAxSelectCall16 call = reinterpret_cast<CuteQAxSelectCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAxSelectCall17 call = reinterpret_cast<CuteQAxSelectCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAxSelectCall18 call = reinterpret_cast<CuteQAxSelectCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAxSelectCall19 call = reinterpret_cast<CuteQAxSelectCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAxSelectCall20 call = reinterpret_cast<CuteQAxSelectCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAxSelectCall21 call = reinterpret_cast<CuteQAxSelectCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAxSelectCall22 call = reinterpret_cast<CuteQAxSelectCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAxSelectCall23 call = reinterpret_cast<CuteQAxSelectCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAxSelectCall24 call = reinterpret_cast<CuteQAxSelectCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAxSelectCall25 call = reinterpret_cast<CuteQAxSelectCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAxSelectCall26 call = reinterpret_cast<CuteQAxSelectCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAxSelectCall27 call = reinterpret_cast<CuteQAxSelectCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAxSelectCall28 call = reinterpret_cast<CuteQAxSelectCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAxSelectCall29 call = reinterpret_cast<CuteQAxSelectCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAxSelectCall30 call = reinterpret_cast<CuteQAxSelectCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAxSelectCall31 call = reinterpret_cast<CuteQAxSelectCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAxSelectCall32 call = reinterpret_cast<CuteQAxSelectCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAxSelectCall33 call = reinterpret_cast<CuteQAxSelectCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAxSelectCall34 call = reinterpret_cast<CuteQAxSelectCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAxSelectCall35 call = reinterpret_cast<CuteQAxSelectCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAxSelectCall36 call = reinterpret_cast<CuteQAxSelectCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAxSelectCall37 call = reinterpret_cast<CuteQAxSelectCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAxSelectCall38 call = reinterpret_cast<CuteQAxSelectCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAxSelectCall39 call = reinterpret_cast<CuteQAxSelectCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQAxSelectCall40 call = reinterpret_cast<CuteQAxSelectCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQAxSelectCall41 call = reinterpret_cast<CuteQAxSelectCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQAxSelectCall42 call = reinterpret_cast<CuteQAxSelectCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAxSelectCall43 call = reinterpret_cast<CuteQAxSelectCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQAxSelectCall44 call = reinterpret_cast<CuteQAxSelectCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQAxSelectCall45 call = reinterpret_cast<CuteQAxSelectCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQAxSelectCall46 call = reinterpret_cast<CuteQAxSelectCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQAxSelectCall47 call = reinterpret_cast<CuteQAxSelectCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQAxSelectCall48 call = reinterpret_cast<CuteQAxSelectCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQAxSelectCall49 call = reinterpret_cast<CuteQAxSelectCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQAxSelectCall50 call = reinterpret_cast<CuteQAxSelectCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAxSelect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QAxSelect10metaObjectEv(
    const QAxSelect *self) {
  return self->metaObject();
}

//  QString QAxSelect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QAxSelect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAxSelect::tr(s, c, n));
}

//  QAxSelect::QAxSelect(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QAxSelect *ritual_ZN9QAxSelectC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQAxSelect(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QAxSelect::~QAxSelect()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxSelectD1Ev(QAxSelect *self) {
  delete self;
}

//  QString QAxSelect::clsid() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QAxSelect5clsidEv(const QAxSelect *self) {
  return new QString(self->clsid());
}

//  SandboxingLevel QAxSelect::sandboxingLevel() const
extern "C" Q_DECL_EXPORT
QAxSelect::SandboxingLevel ritual_ZNK9QAxSelect15sandboxingLevelEv(
    const QAxSelect *self) {
  return self->sandboxingLevel();
}

//  void QAxSelect::onActiveXListCurrentChanged(const QModelIndex &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxSelect27onActiveXListCurrentChangedERK11QModelIndex(
    QAxSelect *self,
    const QModelIndex *a0) {
  self->onActiveXListCurrentChanged(*a0);
}

//  void QAxSelect::onActiveXListActivated()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxSelect22onActiveXListActivatedEv(QAxSelect *self) {
  self->onActiveXListActivated();
}

//  void QAxSelect::onFilterLineEditChanged(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxSelect23onFilterLineEditChangedERK7QString(
    QAxSelect *self,
    const QString *a0) {
  self->onFilterLineEditChanged(*a0);
}

//  a Python function taken by a CuteQAxSelect, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxSelect(QAxSelect *self, const char *key, void *call) {
  return static_cast<CuteQAxSelect *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
