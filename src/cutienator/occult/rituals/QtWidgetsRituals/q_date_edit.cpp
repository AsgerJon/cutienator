//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatetimeedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDateEdit that Python can take functions over in. Every QDateEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQDateEditCall0)(const void *, int *);
typedef void (*CuteQDateEditCall1)(const void *, int *);
typedef void (*CuteQDateEditCall2)(const void *, int, int *);
typedef bool (*CuteQDateEditCall3)(const void *, QEvent *, int *);
typedef void (*CuteQDateEditCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDateEditCall5)(const void *, QWheelEvent *, int *);
typedef void (*CuteQDateEditCall6)(const void *, QFocusEvent *, int *);
typedef bool (*CuteQDateEditCall7)(const void *, bool, int *);
typedef const QDateTime * (*CuteQDateEditCall8)(const void *, const QString *, int *);
typedef QString * (*CuteQDateEditCall9)(const void *, const QDateTime *, int *);
typedef int (*CuteQDateEditCall10)(const void *, int *);
typedef void (*CuteQDateEditCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateEditCall12)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDateEditCall13)(const void *, QStyleOptionSpinBox *, int *);
typedef const QSize * (*CuteQDateEditCall14)(const void *, int *);
typedef const QVariant * (*CuteQDateEditCall15)(const void *, int, int *);
typedef void (*CuteQDateEditCall16)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDateEditCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDateEditCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDateEditCall19)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQDateEditCall20)(const void *, QEvent *, int *);
typedef void (*CuteQDateEditCall21)(const void *, QCloseEvent *, int *);
typedef void (*CuteQDateEditCall22)(const void *, QHideEvent *, int *);
typedef void (*CuteQDateEditCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateEditCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateEditCall25)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDateEditCall26)(const void *, QShowEvent *, int *);
typedef int (*CuteQDateEditCall27)(const void *, int *);
typedef void (*CuteQDateEditCall28)(const void *, bool, int *);
typedef int (*CuteQDateEditCall29)(const void *, int, int *);
typedef bool (*CuteQDateEditCall30)(const void *, int *);
typedef void * (*CuteQDateEditCall31)(const void *, int *);
typedef void (*CuteQDateEditCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDateEditCall33)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDateEditCall34)(const void *, QEvent *, int *);
typedef void (*CuteQDateEditCall35)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDateEditCall36)(const void *, QTabletEvent *, int *);
typedef void (*CuteQDateEditCall37)(const void *, QActionEvent *, int *);
typedef void (*CuteQDateEditCall38)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQDateEditCall39)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQDateEditCall40)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQDateEditCall41)(const void *, QDropEvent *, int *);
typedef int (*CuteQDateEditCall42)(const void *, int, int *);
typedef void (*CuteQDateEditCall43)(const void *, QPainter *, int *);
typedef void * (*CuteQDateEditCall44)(const void *, QPoint *, int *);
typedef void * (*CuteQDateEditCall45)(const void *, int *);
typedef void (*CuteQDateEditCall46)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQDateEditCall47)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDateEditCall48)(const void *, QChildEvent *, int *);
typedef void (*CuteQDateEditCall49)(const void *, QEvent *, int *);
typedef void (*CuteQDateEditCall50)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDateEditCall51)(const void *, const QMetaMethod *, int *);
class CuteQDateEdit : public QDateEdit {
public:
  using QDateEdit::QDateEdit;
  void *taken[52] = {};

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
    if (!std::strcmp(key, "_ZNK13QDateTimeEdit16dateTimeFromTextERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QDateTimeEdit16textFromDateTimeERK9QDateTime")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox11stepEnabledEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
    return false;
  }

  //  QSize QDateTimeEdit::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateEditCall0 call = reinterpret_cast<CuteQDateEditCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEdit::sizeHint();
  }

  //  void QDateTimeEdit::clear()
  void clear() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateEditCall1 call = reinterpret_cast<CuteQDateEditCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDateTimeEdit::clear();
  }

  //  void QDateTimeEdit::stepBy(int steps)
  void stepBy(int steps) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDateEditCall2 call = reinterpret_cast<CuteQDateEditCall2>(taken[2]);
      call(this, steps, &handled);
      if (handled) return;
    }
    QDateTimeEdit::stepBy(steps);
  }

  //  bool QDateTimeEdit::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDateEditCall3 call = reinterpret_cast<CuteQDateEditCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QDateTimeEdit::event(event);
  }

  //  void QDateTimeEdit::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDateEditCall4 call = reinterpret_cast<CuteQDateEditCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::keyPressEvent(event);
  }

  //  void QDateTimeEdit::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDateEditCall5 call = reinterpret_cast<CuteQDateEditCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::wheelEvent(event);
  }

  //  void QDateTimeEdit::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDateEditCall6 call = reinterpret_cast<CuteQDateEditCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::focusInEvent(event);
  }

  //  bool QDateTimeEdit::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDateEditCall7 call = reinterpret_cast<CuteQDateEditCall7>(taken[7]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QDateTimeEdit::focusNextPrevChild(next);
  }

  //  QDateTime QDateTimeEdit::dateTimeFromText(const QString &text) const
  QDateTime dateTimeFromText(const QString &text) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDateEditCall8 call = reinterpret_cast<CuteQDateEditCall8>(taken[8]);
      const QDateTime * given = call(this, &text, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEdit::dateTimeFromText(text);
  }

  //  QString QDateTimeEdit::textFromDateTime(const QDateTime &dt) const
  QString textFromDateTime(const QDateTime &dt) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDateEditCall9 call = reinterpret_cast<CuteQDateEditCall9>(taken[9]);
      QString * given = call(this, &dt, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDateTimeEdit::textFromDateTime(dt);
  }

  //  StepEnabled QDateTimeEdit::stepEnabled() const
  QAbstractSpinBox::StepEnabled stepEnabled() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDateEditCall10 call = reinterpret_cast<CuteQDateEditCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstractSpinBox::StepEnabledFlag>::fromInt(given);
    }
    return QDateTimeEdit::stepEnabled();
  }

  //  void QDateTimeEdit::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDateEditCall11 call = reinterpret_cast<CuteQDateEditCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::mousePressEvent(event);
  }

  //  void QDateTimeEdit::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDateEditCall12 call = reinterpret_cast<CuteQDateEditCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDateTimeEdit::paintEvent(event);
  }

  //  void QDateTimeEdit::initStyleOption(QStyleOptionSpinBox *option)
  //      const
  void initStyleOption(QStyleOptionSpinBox *option) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDateEditCall13 call = reinterpret_cast<CuteQDateEditCall13>(taken[13]);
      call(this, option, &handled);
      if (handled) return;
    }
    QDateTimeEdit::initStyleOption(option);
  }

  //  QSize QAbstractSpinBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDateEditCall14 call = reinterpret_cast<CuteQDateEditCall14>(taken[14]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::minimumSizeHint();
  }

  //  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDateEditCall15 call = reinterpret_cast<CuteQDateEditCall15>(taken[15]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::inputMethodQuery(a0);
  }

  //  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDateEditCall16 call = reinterpret_cast<CuteQDateEditCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::resizeEvent(event);
  }

  //  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDateEditCall17 call = reinterpret_cast<CuteQDateEditCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyReleaseEvent(event);
  }

  //  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDateEditCall18 call = reinterpret_cast<CuteQDateEditCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusOutEvent(event);
  }

  //  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDateEditCall19 call = reinterpret_cast<CuteQDateEditCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::contextMenuEvent(event);
  }

  //  void QAbstractSpinBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDateEditCall20 call = reinterpret_cast<CuteQDateEditCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::changeEvent(event);
  }

  //  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDateEditCall21 call = reinterpret_cast<CuteQDateEditCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::closeEvent(event);
  }

  //  void QAbstractSpinBox::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDateEditCall22 call = reinterpret_cast<CuteQDateEditCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::hideEvent(event);
  }

  //  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDateEditCall23 call = reinterpret_cast<CuteQDateEditCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseReleaseEvent(event);
  }

  //  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDateEditCall24 call = reinterpret_cast<CuteQDateEditCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseMoveEvent(event);
  }

  //  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDateEditCall25 call = reinterpret_cast<CuteQDateEditCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::timerEvent(event);
  }

  //  void QAbstractSpinBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDateEditCall26 call = reinterpret_cast<CuteQDateEditCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::showEvent(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQDateEditCall27 call = reinterpret_cast<CuteQDateEditCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDateEditCall28 call = reinterpret_cast<CuteQDateEditCall28>(taken[28]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQDateEditCall29 call = reinterpret_cast<CuteQDateEditCall29>(taken[29]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQDateEditCall30 call = reinterpret_cast<CuteQDateEditCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQDateEditCall31 call = reinterpret_cast<CuteQDateEditCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDateEditCall32 call = reinterpret_cast<CuteQDateEditCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDateEditCall33 call = reinterpret_cast<CuteQDateEditCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDateEditCall34 call = reinterpret_cast<CuteQDateEditCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDateEditCall35 call = reinterpret_cast<CuteQDateEditCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDateEditCall36 call = reinterpret_cast<CuteQDateEditCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDateEditCall37 call = reinterpret_cast<CuteQDateEditCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDateEditCall38 call = reinterpret_cast<CuteQDateEditCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDateEditCall39 call = reinterpret_cast<CuteQDateEditCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDateEditCall40 call = reinterpret_cast<CuteQDateEditCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDateEditCall41 call = reinterpret_cast<CuteQDateEditCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQDateEditCall42 call = reinterpret_cast<CuteQDateEditCall42>(taken[42]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQDateEditCall43 call = reinterpret_cast<CuteQDateEditCall43>(taken[43]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQDateEditCall44 call = reinterpret_cast<CuteQDateEditCall44>(taken[44]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQDateEditCall45 call = reinterpret_cast<CuteQDateEditCall45>(taken[45]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDateEditCall46 call = reinterpret_cast<CuteQDateEditCall46>(taken[46]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDateEditCall47 call = reinterpret_cast<CuteQDateEditCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQDateEditCall48 call = reinterpret_cast<CuteQDateEditCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQDateEditCall49 call = reinterpret_cast<CuteQDateEditCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQDateEditCall50 call = reinterpret_cast<CuteQDateEditCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQDateEditCall51 call = reinterpret_cast<CuteQDateEditCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDateEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QDateEdit10metaObjectEv(
    const QDateEdit *self) {
  return self->metaObject();
}

//  QString QDateEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QDateEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDateEdit::tr(s, c, n));
}

//  QDateEdit::QDateEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateEdit *ritual_ZN9QDateEditC1EP7QWidget(QWidget *parent) {
  return new CuteQDateEdit(parent);
}

//  QDateEdit::QDateEdit(QDate date, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateEdit *ritual_ZN9QDateEditC1E5QDateP7QWidget(
    const QDate *date,
    QWidget *parent) {
  return new CuteQDateEdit(*date, parent);
}

//  QDateEdit::~QDateEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateEditD1Ev(QDateEdit *self) {
  delete self;
}

//  a Python function taken by a CuteQDateEdit, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateEdit(QDateEdit *self, const char *key, void *call) {
  return static_cast<CuteQDateEdit *>(self)->take(key, call);
}
