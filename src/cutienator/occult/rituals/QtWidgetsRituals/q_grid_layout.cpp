//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgridlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgridlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGridLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGridLayout : QGridLayout {
  using QGridLayout::addItem;
};

//  A QGridLayout that Python can take functions over in. Every QGridLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQGridLayoutCall0)(const void *, int *);
typedef const QSize * (*CuteQGridLayoutCall1)(const void *, int *);
typedef const QSize * (*CuteQGridLayoutCall2)(const void *, int *);
typedef void (*CuteQGridLayoutCall3)(const void *, int, int *);
typedef int (*CuteQGridLayoutCall4)(const void *, int *);
typedef bool (*CuteQGridLayoutCall5)(const void *, int *);
typedef int (*CuteQGridLayoutCall6)(const void *, int, int *);
typedef int (*CuteQGridLayoutCall7)(const void *, int, int *);
typedef int (*CuteQGridLayoutCall8)(const void *, int *);
typedef void (*CuteQGridLayoutCall9)(const void *, int *);
typedef void * (*CuteQGridLayoutCall10)(const void *, int, int *);
typedef void * (*CuteQGridLayoutCall11)(const void *, int, int *);
typedef int (*CuteQGridLayoutCall12)(const void *, int *);
typedef void (*CuteQGridLayoutCall13)(const void *, const QRect *, int *);
typedef void (*CuteQGridLayoutCall14)(const void *, QLayoutItem *, int *);
typedef const QRect * (*CuteQGridLayoutCall15)(const void *, int *);
typedef int (*CuteQGridLayoutCall16)(const void *, const QWidget *, int *);
typedef int (*CuteQGridLayoutCall17)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQGridLayoutCall18)(const void *, int *);
typedef int (*CuteQGridLayoutCall19)(const void *, int *);
typedef void * (*CuteQGridLayoutCall20)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQGridLayoutCall21)(const void *, int *);
typedef void (*CuteQGridLayoutCall22)(const void *, QChildEvent *, int *);
typedef bool (*CuteQGridLayoutCall23)(const void *, QEvent *, int *);
typedef bool (*CuteQGridLayoutCall24)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGridLayoutCall25)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGridLayoutCall26)(const void *, QEvent *, int *);
typedef void (*CuteQGridLayoutCall27)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGridLayoutCall28)(const void *, const QMetaMethod *, int *);
typedef void * (*CuteQGridLayoutCall29)(const void *, int *);
typedef void * (*CuteQGridLayoutCall30)(const void *, int *);
class CuteQGridLayout : public QGridLayout {
public:
  using QGridLayout::QGridLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[30] = call;
      return true;
    }
    return false;
  }

  //  QSize QGridLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGridLayoutCall0 call = reinterpret_cast<CuteQGridLayoutCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGridLayout::sizeHint();
  }

  //  QSize QGridLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGridLayoutCall1 call = reinterpret_cast<CuteQGridLayoutCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGridLayout::minimumSize();
  }

  //  QSize QGridLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGridLayoutCall2 call = reinterpret_cast<CuteQGridLayoutCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGridLayout::maximumSize();
  }

  //  void QGridLayout::setSpacing(int spacing)
  void setSpacing(int spacing) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGridLayoutCall3 call = reinterpret_cast<CuteQGridLayoutCall3>(taken[3]);
      call(this, spacing, &handled);
      if (handled) return;
    }
    QGridLayout::setSpacing(spacing);
  }

  //  int QGridLayout::spacing() const
  int spacing() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGridLayoutCall4 call = reinterpret_cast<CuteQGridLayoutCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGridLayout::spacing();
  }

  //  bool QGridLayout::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGridLayoutCall5 call = reinterpret_cast<CuteQGridLayoutCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGridLayout::hasHeightForWidth();
  }

  //  int QGridLayout::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGridLayoutCall6 call = reinterpret_cast<CuteQGridLayoutCall6>(taken[6]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QGridLayout::heightForWidth(a0);
  }

  //  int QGridLayout::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGridLayoutCall7 call = reinterpret_cast<CuteQGridLayoutCall7>(taken[7]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QGridLayout::minimumHeightForWidth(a0);
  }

  //  Qt::Orientations QGridLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGridLayoutCall8 call = reinterpret_cast<CuteQGridLayoutCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QGridLayout::expandingDirections();
  }

  //  void QGridLayout::invalidate()
  void invalidate() override {
    if (taken[9]) {
      int handled = 0;
      CuteQGridLayoutCall9 call = reinterpret_cast<CuteQGridLayoutCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QGridLayout::invalidate();
  }

  //  QLayoutItem *QGridLayout::itemAt(int index) const
  QLayoutItem *itemAt(int index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGridLayoutCall10 call = reinterpret_cast<CuteQGridLayoutCall10>(taken[10]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QGridLayout::itemAt(index);
  }

  //  QLayoutItem *QGridLayout::takeAt(int index)
  QLayoutItem *takeAt(int index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGridLayoutCall11 call = reinterpret_cast<CuteQGridLayoutCall11>(taken[11]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QGridLayout::takeAt(index);
  }

  //  int QGridLayout::count() const
  int count() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGridLayoutCall12 call = reinterpret_cast<CuteQGridLayoutCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGridLayout::count();
  }

  //  void QGridLayout::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGridLayoutCall13 call = reinterpret_cast<CuteQGridLayoutCall13>(taken[13]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QGridLayout::setGeometry(a0);
  }

  //  void QGridLayout::addItem(QLayoutItem *a0)
  void addItem(QLayoutItem *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGridLayoutCall14 call = reinterpret_cast<CuteQGridLayoutCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGridLayout::addItem(a0);
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGridLayoutCall15 call = reinterpret_cast<CuteQGridLayoutCall15>(taken[15]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGridLayoutCall16 call = reinterpret_cast<CuteQGridLayoutCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGridLayoutCall17 call = reinterpret_cast<CuteQGridLayoutCall17>(taken[17]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQGridLayoutCall18 call = reinterpret_cast<CuteQGridLayoutCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQGridLayoutCall19 call = reinterpret_cast<CuteQGridLayoutCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QLayout::controlTypes();
  }

  //  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
  //      Qt::FindChildOptions options)
  QLayoutItem *replaceWidget(
      QWidget *from,
      QWidget *to,
      Qt::FindChildOptions options) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGridLayoutCall20 call = reinterpret_cast<CuteQGridLayoutCall20>(taken[20]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[21]) {
      int handled = 0;
      CuteQGridLayoutCall21 call = reinterpret_cast<CuteQGridLayoutCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGridLayoutCall22 call = reinterpret_cast<CuteQGridLayoutCall22>(taken[22]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGridLayoutCall23 call = reinterpret_cast<CuteQGridLayoutCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGridLayoutCall24 call = reinterpret_cast<CuteQGridLayoutCall24>(taken[24]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGridLayoutCall25 call = reinterpret_cast<CuteQGridLayoutCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGridLayoutCall26 call = reinterpret_cast<CuteQGridLayoutCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGridLayoutCall27 call = reinterpret_cast<CuteQGridLayoutCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGridLayoutCall28 call = reinterpret_cast<CuteQGridLayoutCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQGridLayoutCall29 call = reinterpret_cast<CuteQGridLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQGridLayoutCall30 call = reinterpret_cast<CuteQGridLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QGridLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QGridLayout10metaObjectEv(
    const QGridLayout *self) {
  return self->metaObject();
}

//  QString QGridLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QGridLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGridLayout::tr(s, c, n));
}

//  QGridLayout::QGridLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QGridLayout *ritual_ZN11QGridLayoutC1EP7QWidget(QWidget *parent) {
  return new CuteQGridLayout(parent);
}

//  QGridLayout::~QGridLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayoutD1Ev(QGridLayout *self) {
  delete self;
}

//  QSize QGridLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QGridLayout8sizeHintEv(const QGridLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QGridLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QGridLayout11minimumSizeEv(const QGridLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QGridLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QGridLayout11maximumSizeEv(const QGridLayout *self) {
  return new QSize(self->maximumSize());
}

//  void QGridLayout::setHorizontalSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout20setHorizontalSpacingEi(
    QGridLayout *self,
    int spacing) {
  self->setHorizontalSpacing(spacing);
}

//  int QGridLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout17horizontalSpacingEv(const QGridLayout *self) {
  return self->horizontalSpacing();
}

//  void QGridLayout::setVerticalSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout18setVerticalSpacingEi(
    QGridLayout *self,
    int spacing) {
  self->setVerticalSpacing(spacing);
}

//  int QGridLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout15verticalSpacingEv(const QGridLayout *self) {
  return self->verticalSpacing();
}

//  void QGridLayout::setSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout10setSpacingEi(QGridLayout *self, int spacing) {
  self->setSpacing(spacing);
}

//  int QGridLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout7spacingEv(const QGridLayout *self) {
  return self->spacing();
}

//  void QGridLayout::setRowStretch(int row, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout13setRowStretchEii(
    QGridLayout *self,
    int row,
    int stretch) {
  self->setRowStretch(row, stretch);
}

//  void QGridLayout::setColumnStretch(int column, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout16setColumnStretchEii(
    QGridLayout *self,
    int column,
    int stretch) {
  self->setColumnStretch(column, stretch);
}

//  int QGridLayout::rowStretch(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout10rowStretchEi(const QGridLayout *self, int row) {
  return self->rowStretch(row);
}

//  int QGridLayout::columnStretch(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout13columnStretchEi(
    const QGridLayout *self,
    int column) {
  return self->columnStretch(column);
}

//  void QGridLayout::setRowMinimumHeight(int row, int minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout19setRowMinimumHeightEii(
    QGridLayout *self,
    int row,
    int minSize) {
  self->setRowMinimumHeight(row, minSize);
}

//  void QGridLayout::setColumnMinimumWidth(int column, int minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout21setColumnMinimumWidthEii(
    QGridLayout *self,
    int column,
    int minSize) {
  self->setColumnMinimumWidth(column, minSize);
}

//  int QGridLayout::rowMinimumHeight(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout16rowMinimumHeightEi(
    const QGridLayout *self,
    int row) {
  return self->rowMinimumHeight(row);
}

//  int QGridLayout::columnMinimumWidth(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout18columnMinimumWidthEi(
    const QGridLayout *self,
    int column) {
  return self->columnMinimumWidth(column);
}

//  int QGridLayout::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout11columnCountEv(const QGridLayout *self) {
  return self->columnCount();
}

//  int QGridLayout::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout8rowCountEv(const QGridLayout *self) {
  return self->rowCount();
}

//  QRect QGridLayout::cellRect(int row, int column) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QGridLayout8cellRectEii(
    const QGridLayout *self,
    int row,
    int column) {
  return new QRect(self->cellRect(row, column));
}

//  bool QGridLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGridLayout17hasHeightForWidthEv(const QGridLayout *self) {
  return self->hasHeightForWidth();
}

//  int QGridLayout::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout14heightForWidthEi(
    const QGridLayout *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QGridLayout::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout21minimumHeightForWidthEi(
    const QGridLayout *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  Qt::Orientations QGridLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout19expandingDirectionsEv(const QGridLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QGridLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout10invalidateEv(QGridLayout *self) {
  self->invalidate();
}

//  void QGridLayout::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addWidgetEP7QWidget(
    QGridLayout *self,
    QWidget *w) {
  self->addWidget(w);
}

//  void QGridLayout::addWidget(QWidget *a0, int row, int column,
//      Qt::Alignment a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addWidgetEP7QWidgetii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QWidget *a0,
    int row,
    int column,
    int a3) {
  self->addWidget(a0, row, column, QFlags<Qt::AlignmentFlag>::fromInt(a3));
}

//  void QGridLayout::addWidget(QWidget *a0, int row, int column, int
//      rowSpan, int columnSpan, Qt::Alignment a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addWidgetEP7QWidgetiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QWidget *a0,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int a5) {
  self->addWidget(
      a0,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(a5));
}

//  void QGridLayout::addLayout(QLayout *a0, int row, int column,
//      Qt::Alignment a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addLayoutEP7QLayoutii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QLayout *a0,
    int row,
    int column,
    int a3) {
  self->addLayout(a0, row, column, QFlags<Qt::AlignmentFlag>::fromInt(a3));
}

//  void QGridLayout::addLayout(QLayout *a0, int row, int column, int
//      rowSpan, int columnSpan, Qt::Alignment a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addLayoutEP7QLayoutiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QLayout *a0,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int a5) {
  self->addLayout(
      a0,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(a5));
}

//  void QGridLayout::setOriginCorner(Qt::Corner a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout15setOriginCornerEN2Qt6CornerE(
    QGridLayout *self,
    Qt::Corner a0) {
  self->setOriginCorner(a0);
}

//  Qt::Corner QGridLayout::originCorner() const
extern "C" Q_DECL_EXPORT
Qt::Corner ritual_ZNK11QGridLayout12originCornerEv(const QGridLayout *self) {
  return self->originCorner();
}

//  QLayoutItem *QGridLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK11QGridLayout6itemAtEi(
    const QGridLayout *self,
    int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QGridLayout::itemAtPosition(int row, int column) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK11QGridLayout14itemAtPositionEii(
    const QGridLayout *self,
    int row,
    int column) {
  return self->itemAtPosition(row, column);
}

//  QLayoutItem *QGridLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN11QGridLayout6takeAtEi(QGridLayout *self, int index) {
  return self->takeAt(index);
}

//  int QGridLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout5countEv(const QGridLayout *self) {
  return self->count();
}

//  void QGridLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout11setGeometryERK5QRect(
    QGridLayout *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  void QGridLayout::addItem(QLayoutItem *item, int row, int column, int
//      rowSpan, int columnSpan, Qt::Alignment a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout7addItemEP11QLayoutItemiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QLayoutItem *item,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int a5) {
  self->addItem(
      item,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(a5));
}

//  void QGridLayout::setDefaultPositioning(int n, Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout21setDefaultPositioningEiN2Qt11OrientationE(
    QGridLayout *self,
    int n,
    Qt::Orientation orient) {
  self->setDefaultPositioning(n, orient);
}

//  void QGridLayout::getItemPosition(int idx, int *row, int *column, int
//      *rowSpan, int *columnSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QGridLayout15getItemPositionEiPiS0_S0_S0_(
    const QGridLayout *self,
    int idx,
    int *row,
    int *column,
    int *rowSpan,
    int *columnSpan) {
  self->getItemPosition(idx, row, column, rowSpan, columnSpan);
}

//  void QGridLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout7addItemEP11QLayoutItem(
    QGridLayout *self,
    QLayoutItem *a0) {
  self->addItem(a0);
}

//  a Python function taken by a CuteQGridLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGridLayout(
    QGridLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGridLayout *>(self)->take(key, call);
}

//  QSize QGridLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QGridLayout8sizeHintEv(const QGridLayout *self) {
  return new QSize(self->QGridLayout::sizeHint());
}

//  QSize QGridLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QGridLayout11minimumSizeEv(const QGridLayout *self) {
  return new QSize(self->QGridLayout::minimumSize());
}

//  QSize QGridLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QGridLayout11maximumSizeEv(const QGridLayout *self) {
  return new QSize(self->QGridLayout::maximumSize());
}

//  void QGridLayout::setSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGridLayout10setSpacingEi(
    QGridLayout *self,
    int spacing) {
  self->QGridLayout::setSpacing(spacing);
}

//  int QGridLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QGridLayout7spacingEv(const QGridLayout *self) {
  return self->QGridLayout::spacing();
}

//  bool QGridLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QGridLayout17hasHeightForWidthEv(
    const QGridLayout *self) {
  return self->QGridLayout::hasHeightForWidth();
}

//  int QGridLayout::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QGridLayout14heightForWidthEi(
    const QGridLayout *self,
    int a0) {
  return self->QGridLayout::heightForWidth(a0);
}

//  int QGridLayout::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QGridLayout21minimumHeightForWidthEi(
    const QGridLayout *self,
    int a0) {
  return self->QGridLayout::minimumHeightForWidth(a0);
}

//  Qt::Orientations QGridLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QGridLayout19expandingDirectionsEv(
    const QGridLayout *self) {
  return static_cast<int>(self->QGridLayout::expandingDirections().toInt());
}

//  void QGridLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGridLayout10invalidateEv(QGridLayout *self) {
  self->QGridLayout::invalidate();
}

//  QLayoutItem *QGridLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK11QGridLayout6itemAtEi(
    const QGridLayout *self,
    int index) {
  return self->QGridLayout::itemAt(index);
}

//  QLayoutItem *QGridLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN11QGridLayout6takeAtEi(
    QGridLayout *self,
    int index) {
  return self->QGridLayout::takeAt(index);
}

//  int QGridLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QGridLayout5countEv(const QGridLayout *self) {
  return self->QGridLayout::count();
}

//  void QGridLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGridLayout11setGeometryERK5QRect(
    QGridLayout *self,
    const QRect *a0) {
  self->QGridLayout::setGeometry(*a0);
}

//  void QGridLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGridLayout7addItemEP11QLayoutItem(
    QGridLayout *self,
    QLayoutItem *a0) {
  static_cast<OwnQGridLayout *>(self)->OwnQGridLayout::addItem(a0);
}
