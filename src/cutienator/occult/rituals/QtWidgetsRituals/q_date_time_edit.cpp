//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatetimeedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDateTimeEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDateTimeEdit : QDateTimeEdit {
  using QDateTimeEdit::keyPressEvent;
  using QDateTimeEdit::wheelEvent;
  using QDateTimeEdit::focusInEvent;
  using QDateTimeEdit::focusNextPrevChild;
  using QDateTimeEdit::mousePressEvent;
  using QDateTimeEdit::paintEvent;
  using QDateTimeEdit::initStyleOption;
};

//  A QDateTimeEdit that Python can take functions over in. Every QDateTimeEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQDateTimeEditCall0)(const void *, int *);
typedef void (*CuteQDateTimeEditCall1)(const void *, int *);
typedef void (*CuteQDateTimeEditCall2)(const void *, int, int *);
typedef bool (*CuteQDateTimeEditCall3)(const void *, QEvent *, int *);
typedef void (*CuteQDateTimeEditCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDateTimeEditCall5)(const void *, QWheelEvent *, int *);
typedef void (*CuteQDateTimeEditCall6)(const void *, QFocusEvent *, int *);
typedef bool (*CuteQDateTimeEditCall7)(const void *, bool, int *);
typedef void (*CuteQDateTimeEditCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateTimeEditCall9)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDateTimeEditCall10)(const void *, QStyleOptionSpinBox *, int *);
typedef const QSize * (*CuteQDateTimeEditCall11)(const void *, int *);
typedef const QVariant * (*CuteQDateTimeEditCall12)(const void *, int, int *);
typedef void (*CuteQDateTimeEditCall13)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDateTimeEditCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDateTimeEditCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDateTimeEditCall16)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQDateTimeEditCall17)(const void *, QEvent *, int *);
typedef void (*CuteQDateTimeEditCall18)(const void *, QCloseEvent *, int *);
typedef void (*CuteQDateTimeEditCall19)(const void *, QHideEvent *, int *);
typedef void (*CuteQDateTimeEditCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateTimeEditCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateTimeEditCall22)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDateTimeEditCall23)(const void *, QShowEvent *, int *);
typedef int (*CuteQDateTimeEditCall24)(const void *, int *);
typedef void (*CuteQDateTimeEditCall25)(const void *, bool, int *);
typedef int (*CuteQDateTimeEditCall26)(const void *, int, int *);
typedef bool (*CuteQDateTimeEditCall27)(const void *, int *);
typedef void * (*CuteQDateTimeEditCall28)(const void *, int *);
typedef void (*CuteQDateTimeEditCall29)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateTimeEditCall30)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDateTimeEditCall31)(const void *, QEvent *, int *);
typedef void (*CuteQDateTimeEditCall32)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDateTimeEditCall33)(const void *, QTabletEvent *, int *);
typedef void (*CuteQDateTimeEditCall34)(const void *, QActionEvent *, int *);
typedef void (*CuteQDateTimeEditCall35)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQDateTimeEditCall36)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQDateTimeEditCall37)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQDateTimeEditCall38)(const void *, QDropEvent *, int *);
typedef int (*CuteQDateTimeEditCall39)(const void *, int, int *);
typedef void (*CuteQDateTimeEditCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQDateTimeEditCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQDateTimeEditCall42)(const void *, int *);
typedef void (*CuteQDateTimeEditCall43)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQDateTimeEditCall44)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDateTimeEditCall45)(const void *, QChildEvent *, int *);
typedef void (*CuteQDateTimeEditCall46)(const void *, QEvent *, int *);
typedef void (*CuteQDateTimeEditCall47)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDateTimeEditCall48)(const void *, const QMetaMethod *, int *);
class CuteQDateTimeEdit : public QDateTimeEdit {
public:
  using QDateTimeEdit::QDateTimeEdit;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox5clearEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox6stepByEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
    return false;
  }

  //  QSize QDateTimeEdit::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateTimeEditCall0 call = reinterpret_cast<CuteQDateTimeEditCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEdit::sizeHint();
  }

  //  void QDateTimeEdit::clear()
  void clear() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateTimeEditCall1 call = reinterpret_cast<CuteQDateTimeEditCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDateTimeEdit::clear();
  }

  //  void QDateTimeEdit::stepBy(int steps)
  void stepBy(int steps) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDateTimeEditCall2 call = reinterpret_cast<CuteQDateTimeEditCall2>(taken[2]);
      call(this, steps, &handled);
      if (handled) return;
    }
    QDateTimeEdit::stepBy(steps);
  }

  //  bool QDateTimeEdit::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDateTimeEditCall3 call = reinterpret_cast<CuteQDateTimeEditCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QDateTimeEdit::event(event);
  }

  //  void QDateTimeEdit::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDateTimeEditCall4 call = reinterpret_cast<CuteQDateTimeEditCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::keyPressEvent(event);
  }

  //  void QDateTimeEdit::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDateTimeEditCall5 call = reinterpret_cast<CuteQDateTimeEditCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::wheelEvent(event);
  }

  //  void QDateTimeEdit::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDateTimeEditCall6 call = reinterpret_cast<CuteQDateTimeEditCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::focusInEvent(event);
  }

  //  bool QDateTimeEdit::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDateTimeEditCall7 call = reinterpret_cast<CuteQDateTimeEditCall7>(taken[7]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QDateTimeEdit::focusNextPrevChild(next);
  }

  //  void QDateTimeEdit::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDateTimeEditCall8 call = reinterpret_cast<CuteQDateTimeEditCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::mousePressEvent(event);
  }

  //  void QDateTimeEdit::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDateTimeEditCall9 call = reinterpret_cast<CuteQDateTimeEditCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::paintEvent(event);
  }

  //  void QDateTimeEdit::initStyleOption(QStyleOptionSpinBox *option)
  //      const
  void initStyleOption(QStyleOptionSpinBox *option) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDateTimeEditCall10 call = reinterpret_cast<CuteQDateTimeEditCall10>(taken[10]);
      call(this, option, &handled);
      if (handled) return;
    }
    QDateTimeEdit::initStyleOption(option);
  }

  //  QSize QAbstractSpinBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDateTimeEditCall11 call = reinterpret_cast<CuteQDateTimeEditCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::minimumSizeHint();
  }

  //  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDateTimeEditCall12 call = reinterpret_cast<CuteQDateTimeEditCall12>(taken[12]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::inputMethodQuery(a0);
  }

  //  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDateTimeEditCall13 call = reinterpret_cast<CuteQDateTimeEditCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::resizeEvent(event);
  }

  //  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDateTimeEditCall14 call = reinterpret_cast<CuteQDateTimeEditCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyReleaseEvent(event);
  }

  //  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDateTimeEditCall15 call = reinterpret_cast<CuteQDateTimeEditCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusOutEvent(event);
  }

  //  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDateTimeEditCall16 call = reinterpret_cast<CuteQDateTimeEditCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::contextMenuEvent(event);
  }

  //  void QAbstractSpinBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDateTimeEditCall17 call = reinterpret_cast<CuteQDateTimeEditCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::changeEvent(event);
  }

  //  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDateTimeEditCall18 call = reinterpret_cast<CuteQDateTimeEditCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::closeEvent(event);
  }

  //  void QAbstractSpinBox::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDateTimeEditCall19 call = reinterpret_cast<CuteQDateTimeEditCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::hideEvent(event);
  }

  //  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDateTimeEditCall20 call = reinterpret_cast<CuteQDateTimeEditCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseReleaseEvent(event);
  }

  //  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDateTimeEditCall21 call = reinterpret_cast<CuteQDateTimeEditCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseMoveEvent(event);
  }

  //  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDateTimeEditCall22 call = reinterpret_cast<CuteQDateTimeEditCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::timerEvent(event);
  }

  //  void QAbstractSpinBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDateTimeEditCall23 call = reinterpret_cast<CuteQDateTimeEditCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::showEvent(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQDateTimeEditCall24 call = reinterpret_cast<CuteQDateTimeEditCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDateTimeEditCall25 call = reinterpret_cast<CuteQDateTimeEditCall25>(taken[25]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQDateTimeEditCall26 call = reinterpret_cast<CuteQDateTimeEditCall26>(taken[26]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQDateTimeEditCall27 call = reinterpret_cast<CuteQDateTimeEditCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQDateTimeEditCall28 call = reinterpret_cast<CuteQDateTimeEditCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDateTimeEditCall29 call = reinterpret_cast<CuteQDateTimeEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDateTimeEditCall30 call = reinterpret_cast<CuteQDateTimeEditCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDateTimeEditCall31 call = reinterpret_cast<CuteQDateTimeEditCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDateTimeEditCall32 call = reinterpret_cast<CuteQDateTimeEditCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDateTimeEditCall33 call = reinterpret_cast<CuteQDateTimeEditCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDateTimeEditCall34 call = reinterpret_cast<CuteQDateTimeEditCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDateTimeEditCall35 call = reinterpret_cast<CuteQDateTimeEditCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDateTimeEditCall36 call = reinterpret_cast<CuteQDateTimeEditCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDateTimeEditCall37 call = reinterpret_cast<CuteQDateTimeEditCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDateTimeEditCall38 call = reinterpret_cast<CuteQDateTimeEditCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDateTimeEditCall39 call = reinterpret_cast<CuteQDateTimeEditCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQDateTimeEditCall40 call = reinterpret_cast<CuteQDateTimeEditCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQDateTimeEditCall41 call = reinterpret_cast<CuteQDateTimeEditCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQDateTimeEditCall42 call = reinterpret_cast<CuteQDateTimeEditCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDateTimeEditCall43 call = reinterpret_cast<CuteQDateTimeEditCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDateTimeEditCall44 call = reinterpret_cast<CuteQDateTimeEditCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDateTimeEditCall45 call = reinterpret_cast<CuteQDateTimeEditCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDateTimeEditCall46 call = reinterpret_cast<CuteQDateTimeEditCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDateTimeEditCall47 call = reinterpret_cast<CuteQDateTimeEditCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQDateTimeEditCall48 call = reinterpret_cast<CuteQDateTimeEditCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDateTimeEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QDateTimeEdit10metaObjectEv(
    const QDateTimeEdit *self) {
  return self->metaObject();
}

//  QString QDateTimeEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QDateTimeEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDateTimeEdit::tr(s, c, n));
}

//  QDateTimeEdit::QDateTimeEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1EP7QWidget(QWidget *parent) {
  return new CuteQDateTimeEdit(parent);
}

//  QDateTimeEdit::QDateTimeEdit(const QDateTime &dt, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1ERK9QDateTimeP7QWidget(
    const QDateTime *dt,
    QWidget *parent) {
  return new CuteQDateTimeEdit(*dt, parent);
}

//  QDateTimeEdit::QDateTimeEdit(QDate d, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1E5QDateP7QWidget(
    const QDate *d,
    QWidget *parent) {
  return new CuteQDateTimeEdit(*d, parent);
}

//  QDateTimeEdit::QDateTimeEdit(QTime t, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1E5QTimeP7QWidget(
    const QTime *t,
    QWidget *parent) {
  return new CuteQDateTimeEdit(*t, parent);
}

//  QDateTimeEdit::~QDateTimeEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEditD1Ev(QDateTimeEdit *self) {
  delete self;
}

//  QDateTime QDateTimeEdit::dateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeEdit8dateTimeEv(const QDateTimeEdit *self) {
  return new QDateTime(self->dateTime());
}

//  QDate QDateTimeEdit::date() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK13QDateTimeEdit4dateEv(const QDateTimeEdit *self) {
  return new QDate(self->date());
}

//  QTime QDateTimeEdit::time() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK13QDateTimeEdit4timeEv(const QDateTimeEdit *self) {
  return new QTime(self->time());
}

//  QCalendar QDateTimeEdit::calendar() const
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZNK13QDateTimeEdit8calendarEv(const QDateTimeEdit *self) {
  return new QCalendar(self->calendar());
}

//  void QDateTimeEdit::setCalendar(QCalendar calendar)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setCalendarE9QCalendar(
    QDateTimeEdit *self,
    const QCalendar *calendar) {
  self->setCalendar(*calendar);
}

//  QDateTime QDateTimeEdit::minimumDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeEdit15minimumDateTimeEv(
    const QDateTimeEdit *self) {
  return new QDateTime(self->minimumDateTime());
}

//  void QDateTimeEdit::clearMinimumDateTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit20clearMinimumDateTimeEv(QDateTimeEdit *self) {
  self->clearMinimumDateTime();
}

//  void QDateTimeEdit::setMinimumDateTime(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit18setMinimumDateTimeERK9QDateTime(
    QDateTimeEdit *self,
    const QDateTime *dt) {
  self->setMinimumDateTime(*dt);
}

//  QDateTime QDateTimeEdit::maximumDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeEdit15maximumDateTimeEv(
    const QDateTimeEdit *self) {
  return new QDateTime(self->maximumDateTime());
}

//  void QDateTimeEdit::clearMaximumDateTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit20clearMaximumDateTimeEv(QDateTimeEdit *self) {
  self->clearMaximumDateTime();
}

//  void QDateTimeEdit::setMaximumDateTime(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit18setMaximumDateTimeERK9QDateTime(
    QDateTimeEdit *self,
    const QDateTime *dt) {
  self->setMaximumDateTime(*dt);
}

//  void QDateTimeEdit::setDateTimeRange(const QDateTime &min, const
//      QDateTime &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16setDateTimeRangeERK9QDateTimeS2_(
    QDateTimeEdit *self,
    const QDateTime *min,
    const QDateTime *max) {
  self->setDateTimeRange(*min, *max);
}

//  QDate QDateTimeEdit::minimumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK13QDateTimeEdit11minimumDateEv(const QDateTimeEdit *self) {
  return new QDate(self->minimumDate());
}

//  void QDateTimeEdit::setMinimumDate(QDate min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMinimumDateE5QDate(
    QDateTimeEdit *self,
    const QDate *min) {
  self->setMinimumDate(*min);
}

//  void QDateTimeEdit::clearMinimumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMinimumDateEv(QDateTimeEdit *self) {
  self->clearMinimumDate();
}

//  QDate QDateTimeEdit::maximumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK13QDateTimeEdit11maximumDateEv(const QDateTimeEdit *self) {
  return new QDate(self->maximumDate());
}

//  void QDateTimeEdit::setMaximumDate(QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMaximumDateE5QDate(
    QDateTimeEdit *self,
    const QDate *max) {
  self->setMaximumDate(*max);
}

//  void QDateTimeEdit::clearMaximumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMaximumDateEv(QDateTimeEdit *self) {
  self->clearMaximumDate();
}

//  void QDateTimeEdit::setDateRange(QDate min, QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit12setDateRangeE5QDateS0_(
    QDateTimeEdit *self,
    const QDate *min,
    const QDate *max) {
  self->setDateRange(*min, *max);
}

//  QTime QDateTimeEdit::minimumTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK13QDateTimeEdit11minimumTimeEv(const QDateTimeEdit *self) {
  return new QTime(self->minimumTime());
}

//  void QDateTimeEdit::setMinimumTime(QTime min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMinimumTimeE5QTime(
    QDateTimeEdit *self,
    const QTime *min) {
  self->setMinimumTime(*min);
}

//  void QDateTimeEdit::clearMinimumTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMinimumTimeEv(QDateTimeEdit *self) {
  self->clearMinimumTime();
}

//  QTime QDateTimeEdit::maximumTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK13QDateTimeEdit11maximumTimeEv(const QDateTimeEdit *self) {
  return new QTime(self->maximumTime());
}

//  void QDateTimeEdit::setMaximumTime(QTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMaximumTimeE5QTime(
    QDateTimeEdit *self,
    const QTime *max) {
  self->setMaximumTime(*max);
}

//  void QDateTimeEdit::clearMaximumTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMaximumTimeEv(QDateTimeEdit *self) {
  self->clearMaximumTime();
}

//  void QDateTimeEdit::setTimeRange(QTime min, QTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit12setTimeRangeE5QTimeS0_(
    QDateTimeEdit *self,
    const QTime *min,
    const QTime *max) {
  self->setTimeRange(*min, *max);
}

//  Sections QDateTimeEdit::displayedSections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeEdit17displayedSectionsEv(
    const QDateTimeEdit *self) {
  return static_cast<int>(self->displayedSections().toInt());
}

//  Section QDateTimeEdit::currentSection() const
extern "C" Q_DECL_EXPORT
QDateTimeEdit::Section ritual_ZNK13QDateTimeEdit14currentSectionEv(
    const QDateTimeEdit *self) {
  return self->currentSection();
}

//  Section QDateTimeEdit::sectionAt(int index) const
extern "C" Q_DECL_EXPORT
QDateTimeEdit::Section ritual_ZNK13QDateTimeEdit9sectionAtEi(
    const QDateTimeEdit *self,
    int index) {
  return self->sectionAt(index);
}

//  void QDateTimeEdit::setCurrentSection(Section section)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit17setCurrentSectionENS_7SectionE(
    QDateTimeEdit *self,
    QDateTimeEdit::Section section) {
  self->setCurrentSection(section);
}

//  int QDateTimeEdit::currentSectionIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeEdit19currentSectionIndexEv(
    const QDateTimeEdit *self) {
  return self->currentSectionIndex();
}

//  void QDateTimeEdit::setCurrentSectionIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit22setCurrentSectionIndexEi(
    QDateTimeEdit *self,
    int index) {
  self->setCurrentSectionIndex(index);
}

//  QCalendarWidget *QDateTimeEdit::calendarWidget() const
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZNK13QDateTimeEdit14calendarWidgetEv(
    const QDateTimeEdit *self) {
  return self->calendarWidget();
}

//  void QDateTimeEdit::setCalendarWidget(QCalendarWidget *calendarWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit17setCalendarWidgetEP15QCalendarWidget(
    QDateTimeEdit *self,
    QCalendarWidget *calendarWidget) {
  self->setCalendarWidget(calendarWidget);
}

//  int QDateTimeEdit::sectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeEdit12sectionCountEv(const QDateTimeEdit *self) {
  return self->sectionCount();
}

//  void QDateTimeEdit::setSelectedSection(Section section)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit18setSelectedSectionENS_7SectionE(
    QDateTimeEdit *self,
    QDateTimeEdit::Section section) {
  self->setSelectedSection(section);
}

//  QString QDateTimeEdit::sectionText(Section section) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDateTimeEdit11sectionTextENS_7SectionE(
    const QDateTimeEdit *self,
    QDateTimeEdit::Section section) {
  return new QString(self->sectionText(section));
}

//  QString QDateTimeEdit::displayFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDateTimeEdit13displayFormatEv(
    const QDateTimeEdit *self) {
  return new QString(self->displayFormat());
}

//  void QDateTimeEdit::setDisplayFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16setDisplayFormatERK7QString(
    QDateTimeEdit *self,
    const QString *format) {
  self->setDisplayFormat(*format);
}

//  bool QDateTimeEdit::calendarPopup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDateTimeEdit13calendarPopupEv(const QDateTimeEdit *self) {
  return self->calendarPopup();
}

//  void QDateTimeEdit::setCalendarPopup(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16setCalendarPopupEb(
    QDateTimeEdit *self,
    bool enable) {
  self->setCalendarPopup(enable);
}

//  Qt::TimeSpec QDateTimeEdit::timeSpec() const
extern "C" Q_DECL_EXPORT
Qt::TimeSpec ritual_ZNK13QDateTimeEdit8timeSpecEv(
    const QDateTimeEdit *self) {
  return self->timeSpec();
}

//  void QDateTimeEdit::setTimeSpec(Qt::TimeSpec spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setTimeSpecEN2Qt8TimeSpecE(
    QDateTimeEdit *self,
    Qt::TimeSpec spec) {
  self->setTimeSpec(spec);
}

//  QTimeZone QDateTimeEdit::timeZone() const
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZNK13QDateTimeEdit8timeZoneEv(const QDateTimeEdit *self) {
  return new QTimeZone(self->timeZone());
}

//  void QDateTimeEdit::setTimeZone(const QTimeZone &zone)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setTimeZoneERK9QTimeZone(
    QDateTimeEdit *self,
    const QTimeZone *zone) {
  self->setTimeZone(*zone);
}

//  QSize QDateTimeEdit::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QDateTimeEdit8sizeHintEv(const QDateTimeEdit *self) {
  return new QSize(self->sizeHint());
}

//  void QDateTimeEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit5clearEv(QDateTimeEdit *self) {
  self->clear();
}

//  void QDateTimeEdit::stepBy(int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit6stepByEi(QDateTimeEdit *self, int steps) {
  self->stepBy(steps);
}

//  bool QDateTimeEdit::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDateTimeEdit5eventEP6QEvent(
    QDateTimeEdit *self,
    QEvent *event) {
  return self->event(event);
}

//  void QDateTimeEdit::setDateTime(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setDateTimeERK9QDateTime(
    QDateTimeEdit *self,
    const QDateTime *dateTime) {
  self->setDateTime(*dateTime);
}

//  void QDateTimeEdit::setDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit7setDateE5QDate(
    QDateTimeEdit *self,
    const QDate *date) {
  self->setDate(*date);
}

//  void QDateTimeEdit::setTime(QTime time)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit7setTimeE5QTime(
    QDateTimeEdit *self,
    const QTime *time) {
  self->setTime(*time);
}

//  a Python function taken by a CuteQDateTimeEdit, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateTimeEdit(
    QDateTimeEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDateTimeEdit *>(self)->take(key, call);
}

//  QSize QDateTimeEdit::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QDateTimeEdit8sizeHintEv(const QDateTimeEdit *self) {
  return new QSize(self->QDateTimeEdit::sizeHint());
}

//  void QDateTimeEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit5clearEv(QDateTimeEdit *self) {
  self->QDateTimeEdit::clear();
}

//  void QDateTimeEdit::stepBy(int steps)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit6stepByEi(QDateTimeEdit *self, int steps) {
  self->QDateTimeEdit::stepBy(steps);
}

//  bool QDateTimeEdit::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QDateTimeEdit5eventEP6QEvent(
    QDateTimeEdit *self,
    QEvent *event) {
  return self->QDateTimeEdit::event(event);
}

//  void QDateTimeEdit::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit13keyPressEventEP9QKeyEvent(
    QDateTimeEdit *self,
    QKeyEvent *event) {
  static_cast<OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::keyPressEvent(
      event);
}

//  void QDateTimeEdit::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit10wheelEventEP11QWheelEvent(
    QDateTimeEdit *self,
    QWheelEvent *event) {
  static_cast<OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::wheelEvent(event);
}

//  void QDateTimeEdit::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit12focusInEventEP11QFocusEvent(
    QDateTimeEdit *self,
    QFocusEvent *event) {
  static_cast<OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::focusInEvent(
      event);
}

//  bool QDateTimeEdit::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QDateTimeEdit18focusNextPrevChildEb(
    QDateTimeEdit *self,
    bool next) {
  return static_cast<OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::focusNextPrevChild(
      next);
}

//  void QDateTimeEdit::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit15mousePressEventEP11QMouseEvent(
    QDateTimeEdit *self,
    QMouseEvent *event) {
  static_cast<OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::mousePressEvent(
      event);
}

//  void QDateTimeEdit::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDateTimeEdit10paintEventEP11QPaintEvent(
    QDateTimeEdit *self,
    QPaintEvent *event) {
  static_cast<OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::paintEvent(event);
}

//  void QDateTimeEdit::initStyleOption(QStyleOptionSpinBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QDateTimeEdit15initStyleOptionEP19QStyleOptionSpinBox(
    const QDateTimeEdit *self,
    QStyleOptionSpinBox *option) {
  static_cast<const OwnQDateTimeEdit *>(self)->OwnQDateTimeEdit::initStyleOption(
      option);
}
