//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qformlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qformlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFormLayout that Python can take functions over in. Every QFormLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQFormLayoutCall0)(const void *, int *);
typedef void (*CuteQFormLayoutCall1)(const void *, int, int *);
typedef void (*CuteQFormLayoutCall2)(const void *, QLayoutItem *, int *);
typedef void * (*CuteQFormLayoutCall3)(const void *, int, int *);
typedef void * (*CuteQFormLayoutCall4)(const void *, int, int *);
typedef void (*CuteQFormLayoutCall5)(const void *, const QRect *, int *);
typedef const QSize * (*CuteQFormLayoutCall6)(const void *, int *);
typedef const QSize * (*CuteQFormLayoutCall7)(const void *, int *);
typedef void (*CuteQFormLayoutCall8)(const void *, int *);
typedef bool (*CuteQFormLayoutCall9)(const void *, int *);
typedef int (*CuteQFormLayoutCall10)(const void *, int, int *);
typedef int (*CuteQFormLayoutCall11)(const void *, int *);
typedef int (*CuteQFormLayoutCall12)(const void *, int *);
typedef const QRect * (*CuteQFormLayoutCall13)(const void *, int *);
typedef const QSize * (*CuteQFormLayoutCall14)(const void *, int *);
typedef int (*CuteQFormLayoutCall15)(const void *, const QWidget *, int *);
typedef int (*CuteQFormLayoutCall16)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQFormLayoutCall17)(const void *, int *);
typedef int (*CuteQFormLayoutCall18)(const void *, int *);
typedef void * (*CuteQFormLayoutCall19)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQFormLayoutCall20)(const void *, int *);
typedef void (*CuteQFormLayoutCall21)(const void *, QChildEvent *, int *);
typedef bool (*CuteQFormLayoutCall22)(const void *, QEvent *, int *);
typedef bool (*CuteQFormLayoutCall23)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQFormLayoutCall24)(const void *, QTimerEvent *, int *);
typedef void (*CuteQFormLayoutCall25)(const void *, QEvent *, int *);
typedef void (*CuteQFormLayoutCall26)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQFormLayoutCall27)(const void *, const QMetaMethod *, int *);
typedef int (*CuteQFormLayoutCall28)(const void *, int, int *);
typedef void * (*CuteQFormLayoutCall29)(const void *, int *);
typedef void * (*CuteQFormLayoutCall30)(const void *, int *);
class CuteQFormLayout : public QFormLayout {
public:
  using QFormLayout::QFormLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
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

  //  int QFormLayout::spacing() const
  int spacing() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFormLayoutCall0 call = reinterpret_cast<CuteQFormLayoutCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFormLayout::spacing();
  }

  //  void QFormLayout::setSpacing(int a0)
  void setSpacing(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFormLayoutCall1 call = reinterpret_cast<CuteQFormLayoutCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFormLayout::setSpacing(a0);
  }

  //  void QFormLayout::addItem(QLayoutItem *item)
  void addItem(QLayoutItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFormLayoutCall2 call = reinterpret_cast<CuteQFormLayoutCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QFormLayout::addItem(item);
  }

  //  QLayoutItem *QFormLayout::itemAt(int index) const
  QLayoutItem *itemAt(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFormLayoutCall3 call = reinterpret_cast<CuteQFormLayoutCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QFormLayout::itemAt(index);
  }

  //  QLayoutItem *QFormLayout::takeAt(int index)
  QLayoutItem *takeAt(int index) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFormLayoutCall4 call = reinterpret_cast<CuteQFormLayoutCall4>(taken[4]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QFormLayout::takeAt(index);
  }

  //  void QFormLayout::setGeometry(const QRect &rect)
  void setGeometry(const QRect &rect) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFormLayoutCall5 call = reinterpret_cast<CuteQFormLayoutCall5>(taken[5]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QFormLayout::setGeometry(rect);
  }

  //  QSize QFormLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFormLayoutCall6 call = reinterpret_cast<CuteQFormLayoutCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFormLayout::minimumSize();
  }

  //  QSize QFormLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFormLayoutCall7 call = reinterpret_cast<CuteQFormLayoutCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFormLayout::sizeHint();
  }

  //  void QFormLayout::invalidate()
  void invalidate() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFormLayoutCall8 call = reinterpret_cast<CuteQFormLayoutCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QFormLayout::invalidate();
  }

  //  bool QFormLayout::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFormLayoutCall9 call = reinterpret_cast<CuteQFormLayoutCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFormLayout::hasHeightForWidth();
  }

  //  int QFormLayout::heightForWidth(int width) const
  int heightForWidth(int width) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFormLayoutCall10 call = reinterpret_cast<CuteQFormLayoutCall10>(taken[10]);
      int given = call(this, width, &handled);
      if (handled) return given;
    }
    return QFormLayout::heightForWidth(width);
  }

  //  Qt::Orientations QFormLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFormLayoutCall11 call = reinterpret_cast<CuteQFormLayoutCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QFormLayout::expandingDirections();
  }

  //  int QFormLayout::count() const
  int count() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFormLayoutCall12 call = reinterpret_cast<CuteQFormLayoutCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFormLayout::count();
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFormLayoutCall13 call = reinterpret_cast<CuteQFormLayoutCall13>(taken[13]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  QSize QLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFormLayoutCall14 call = reinterpret_cast<CuteQFormLayoutCall14>(taken[14]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::maximumSize();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFormLayoutCall15 call = reinterpret_cast<CuteQFormLayoutCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFormLayoutCall16 call = reinterpret_cast<CuteQFormLayoutCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQFormLayoutCall17 call = reinterpret_cast<CuteQFormLayoutCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQFormLayoutCall18 call = reinterpret_cast<CuteQFormLayoutCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQFormLayoutCall19 call = reinterpret_cast<CuteQFormLayoutCall19>(taken[19]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[20]) {
      int handled = 0;
      CuteQFormLayoutCall20 call = reinterpret_cast<CuteQFormLayoutCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFormLayoutCall21 call = reinterpret_cast<CuteQFormLayoutCall21>(taken[21]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFormLayoutCall22 call = reinterpret_cast<CuteQFormLayoutCall22>(taken[22]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFormLayoutCall23 call = reinterpret_cast<CuteQFormLayoutCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFormLayoutCall24 call = reinterpret_cast<CuteQFormLayoutCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFormLayoutCall25 call = reinterpret_cast<CuteQFormLayoutCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFormLayoutCall26 call = reinterpret_cast<CuteQFormLayoutCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFormLayoutCall27 call = reinterpret_cast<CuteQFormLayoutCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQFormLayoutCall28 call = reinterpret_cast<CuteQFormLayoutCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQFormLayoutCall29 call = reinterpret_cast<CuteQFormLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQFormLayoutCall30 call = reinterpret_cast<CuteQFormLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QFormLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFormLayout10metaObjectEv(
    const QFormLayout *self) {
  return self->metaObject();
}

//  QString QFormLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFormLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFormLayout::tr(s, c, n));
}

//  QFormLayout::QFormLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFormLayout *ritual_ZN11QFormLayoutC1EP7QWidget(QWidget *parent) {
  return new CuteQFormLayout(parent);
}

//  QFormLayout::~QFormLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayoutD1Ev(QFormLayout *self) {
  delete self;
}

//  void QFormLayout::setFieldGrowthPolicy(FieldGrowthPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout20setFieldGrowthPolicyENS_17FieldGrowthPolicyE(
    QFormLayout *self,
    QFormLayout::FieldGrowthPolicy policy) {
  self->setFieldGrowthPolicy(policy);
}

//  FieldGrowthPolicy QFormLayout::fieldGrowthPolicy() const
extern "C" Q_DECL_EXPORT
QFormLayout::FieldGrowthPolicy ritual_ZNK11QFormLayout17fieldGrowthPolicyEv(
    const QFormLayout *self) {
  return self->fieldGrowthPolicy();
}

//  void QFormLayout::setRowWrapPolicy(RowWrapPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout16setRowWrapPolicyENS_13RowWrapPolicyE(
    QFormLayout *self,
    QFormLayout::RowWrapPolicy policy) {
  self->setRowWrapPolicy(policy);
}

//  RowWrapPolicy QFormLayout::rowWrapPolicy() const
extern "C" Q_DECL_EXPORT
QFormLayout::RowWrapPolicy ritual_ZNK11QFormLayout13rowWrapPolicyEv(
    const QFormLayout *self) {
  return self->rowWrapPolicy();
}

//  void QFormLayout::setLabelAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout17setLabelAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QFormLayout *self,
    int alignment) {
  self->setLabelAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QFormLayout::labelAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout14labelAlignmentEv(const QFormLayout *self) {
  return static_cast<int>(self->labelAlignment().toInt());
}

//  void QFormLayout::setFormAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout16setFormAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QFormLayout *self,
    int alignment) {
  self->setFormAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QFormLayout::formAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout13formAlignmentEv(const QFormLayout *self) {
  return static_cast<int>(self->formAlignment().toInt());
}

//  void QFormLayout::setHorizontalSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout20setHorizontalSpacingEi(
    QFormLayout *self,
    int spacing) {
  self->setHorizontalSpacing(spacing);
}

//  int QFormLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout17horizontalSpacingEv(const QFormLayout *self) {
  return self->horizontalSpacing();
}

//  void QFormLayout::setVerticalSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout18setVerticalSpacingEi(
    QFormLayout *self,
    int spacing) {
  self->setVerticalSpacing(spacing);
}

//  int QFormLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout15verticalSpacingEv(const QFormLayout *self) {
  return self->verticalSpacing();
}

//  int QFormLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout7spacingEv(const QFormLayout *self) {
  return self->spacing();
}

//  void QFormLayout::setSpacing(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout10setSpacingEi(QFormLayout *self, int a0) {
  self->setSpacing(a0);
}

//  void QFormLayout::addRow(QWidget *label, QWidget *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout6addRowEP7QWidgetS1_(
    QFormLayout *self,
    QWidget *label,
    QWidget *field) {
  self->addRow(label, field);
}

//  void QFormLayout::addRow(QWidget *label, QLayout *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout6addRowEP7QWidgetP7QLayout(
    QFormLayout *self,
    QWidget *label,
    QLayout *field) {
  self->addRow(label, field);
}

//  void QFormLayout::addRow(const QString &labelText, QWidget *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout6addRowERK7QStringP7QWidget(
    QFormLayout *self,
    const QString *labelText,
    QWidget *field) {
  self->addRow(*labelText, field);
}

//  void QFormLayout::addRow(const QString &labelText, QLayout *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout6addRowERK7QStringP7QLayout(
    QFormLayout *self,
    const QString *labelText,
    QLayout *field) {
  self->addRow(*labelText, field);
}

//  void QFormLayout::addRow(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout6addRowEP7QWidget(
    QFormLayout *self,
    QWidget *widget) {
  self->addRow(widget);
}

//  void QFormLayout::addRow(QLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout6addRowEP7QLayout(
    QFormLayout *self,
    QLayout *layout) {
  self->addRow(layout);
}

//  void QFormLayout::insertRow(int row, QWidget *label, QWidget *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9insertRowEiP7QWidgetS1_(
    QFormLayout *self,
    int row,
    QWidget *label,
    QWidget *field) {
  self->insertRow(row, label, field);
}

//  void QFormLayout::insertRow(int row, QWidget *label, QLayout *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9insertRowEiP7QWidgetP7QLayout(
    QFormLayout *self,
    int row,
    QWidget *label,
    QLayout *field) {
  self->insertRow(row, label, field);
}

//  void QFormLayout::insertRow(int row, const QString &labelText, QWidget
//      *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9insertRowEiRK7QStringP7QWidget(
    QFormLayout *self,
    int row,
    const QString *labelText,
    QWidget *field) {
  self->insertRow(row, *labelText, field);
}

//  void QFormLayout::insertRow(int row, const QString &labelText, QLayout
//      *field)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9insertRowEiRK7QStringP7QLayout(
    QFormLayout *self,
    int row,
    const QString *labelText,
    QLayout *field) {
  self->insertRow(row, *labelText, field);
}

//  void QFormLayout::insertRow(int row, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9insertRowEiP7QWidget(
    QFormLayout *self,
    int row,
    QWidget *widget) {
  self->insertRow(row, widget);
}

//  void QFormLayout::insertRow(int row, QLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9insertRowEiP7QLayout(
    QFormLayout *self,
    int row,
    QLayout *layout) {
  self->insertRow(row, layout);
}

//  void QFormLayout::removeRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9removeRowEi(QFormLayout *self, int row) {
  self->removeRow(row);
}

//  void QFormLayout::removeRow(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9removeRowEP7QWidget(
    QFormLayout *self,
    QWidget *widget) {
  self->removeRow(widget);
}

//  void QFormLayout::removeRow(QLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9removeRowEP7QLayout(
    QFormLayout *self,
    QLayout *layout) {
  self->removeRow(layout);
}

//  TakeRowResult QFormLayout::takeRow(int row)
extern "C" Q_DECL_EXPORT
QFormLayout::TakeRowResult *ritual_ZN11QFormLayout7takeRowEi(
    QFormLayout *self,
    int row) {
  return new QFormLayout::TakeRowResult(self->takeRow(row));
}

//  TakeRowResult QFormLayout::takeRow(QWidget *widget)
extern "C" Q_DECL_EXPORT
QFormLayout::TakeRowResult *ritual_ZN11QFormLayout7takeRowEP7QWidget(
    QFormLayout *self,
    QWidget *widget) {
  return new QFormLayout::TakeRowResult(self->takeRow(widget));
}

//  TakeRowResult QFormLayout::takeRow(QLayout *layout)
extern "C" Q_DECL_EXPORT
QFormLayout::TakeRowResult *ritual_ZN11QFormLayout7takeRowEP7QLayout(
    QFormLayout *self,
    QLayout *layout) {
  return new QFormLayout::TakeRowResult(self->takeRow(layout));
}

//  void QFormLayout::setItem(int row, ItemRole role, QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout7setItemEiNS_8ItemRoleEP11QLayoutItem(
    QFormLayout *self,
    int row,
    QFormLayout::ItemRole role,
    QLayoutItem *item) {
  self->setItem(row, role, item);
}

//  void QFormLayout::setWidget(int row, ItemRole role, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9setWidgetEiNS_8ItemRoleEP7QWidget(
    QFormLayout *self,
    int row,
    QFormLayout::ItemRole role,
    QWidget *widget) {
  self->setWidget(row, role, widget);
}

//  void QFormLayout::setLayout(int row, ItemRole role, QLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout9setLayoutEiNS_8ItemRoleEP7QLayout(
    QFormLayout *self,
    int row,
    QFormLayout::ItemRole role,
    QLayout *layout) {
  self->setLayout(row, role, layout);
}

//  void QFormLayout::setRowVisible(int row, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout13setRowVisibleEib(
    QFormLayout *self,
    int row,
    bool on) {
  self->setRowVisible(row, on);
}

//  void QFormLayout::setRowVisible(QWidget *widget, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout13setRowVisibleEP7QWidgetb(
    QFormLayout *self,
    QWidget *widget,
    bool on) {
  self->setRowVisible(widget, on);
}

//  void QFormLayout::setRowVisible(QLayout *layout, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout13setRowVisibleEP7QLayoutb(
    QFormLayout *self,
    QLayout *layout,
    bool on) {
  self->setRowVisible(layout, on);
}

//  bool QFormLayout::isRowVisible(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFormLayout12isRowVisibleEi(
    const QFormLayout *self,
    int row) {
  return self->isRowVisible(row);
}

//  bool QFormLayout::isRowVisible(QWidget *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFormLayout12isRowVisibleEP7QWidget(
    const QFormLayout *self,
    QWidget *widget) {
  return self->isRowVisible(widget);
}

//  bool QFormLayout::isRowVisible(QLayout *layout) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFormLayout12isRowVisibleEP7QLayout(
    const QFormLayout *self,
    QLayout *layout) {
  return self->isRowVisible(layout);
}

//  QLayoutItem *QFormLayout::itemAt(int row, ItemRole role) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK11QFormLayout6itemAtEiNS_8ItemRoleE(
    const QFormLayout *self,
    int row,
    QFormLayout::ItemRole role) {
  return self->itemAt(row, role);
}

//  QWidget *QFormLayout::labelForField(QWidget *field) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QFormLayout13labelForFieldEP7QWidget(
    const QFormLayout *self,
    QWidget *field) {
  return self->labelForField(field);
}

//  QWidget *QFormLayout::labelForField(QLayout *field) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QFormLayout13labelForFieldEP7QLayout(
    const QFormLayout *self,
    QLayout *field) {
  return self->labelForField(field);
}

//  void QFormLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout7addItemEP11QLayoutItem(
    QFormLayout *self,
    QLayoutItem *item) {
  self->addItem(item);
}

//  QLayoutItem *QFormLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK11QFormLayout6itemAtEi(
    const QFormLayout *self,
    int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QFormLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN11QFormLayout6takeAtEi(QFormLayout *self, int index) {
  return self->takeAt(index);
}

//  void QFormLayout::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout11setGeometryERK5QRect(
    QFormLayout *self,
    const QRect *rect) {
  self->setGeometry(*rect);
}

//  QSize QFormLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QFormLayout11minimumSizeEv(const QFormLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QFormLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QFormLayout8sizeHintEv(const QFormLayout *self) {
  return new QSize(self->sizeHint());
}

//  void QFormLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFormLayout10invalidateEv(QFormLayout *self) {
  self->invalidate();
}

//  bool QFormLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFormLayout17hasHeightForWidthEv(const QFormLayout *self) {
  return self->hasHeightForWidth();
}

//  int QFormLayout::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout14heightForWidthEi(
    const QFormLayout *self,
    int width) {
  return self->heightForWidth(width);
}

//  Qt::Orientations QFormLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout19expandingDirectionsEv(const QFormLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  int QFormLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout5countEv(const QFormLayout *self) {
  return self->count();
}

//  int QFormLayout::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFormLayout8rowCountEv(const QFormLayout *self) {
  return self->rowCount();
}

//  a Python function taken by a CuteQFormLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFormLayout(
    QFormLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFormLayout *>(self)->take(key, call);
}

//  int QFormLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFormLayout7spacingEv(const QFormLayout *self) {
  return self->QFormLayout::spacing();
}

//  void QFormLayout::setSpacing(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFormLayout10setSpacingEi(QFormLayout *self, int a0) {
  self->QFormLayout::setSpacing(a0);
}

//  void QFormLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFormLayout7addItemEP11QLayoutItem(
    QFormLayout *self,
    QLayoutItem *item) {
  self->QFormLayout::addItem(item);
}

//  QLayoutItem *QFormLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK11QFormLayout6itemAtEi(
    const QFormLayout *self,
    int index) {
  return self->QFormLayout::itemAt(index);
}

//  QLayoutItem *QFormLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN11QFormLayout6takeAtEi(
    QFormLayout *self,
    int index) {
  return self->QFormLayout::takeAt(index);
}

//  void QFormLayout::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFormLayout11setGeometryERK5QRect(
    QFormLayout *self,
    const QRect *rect) {
  self->QFormLayout::setGeometry(*rect);
}

//  QSize QFormLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QFormLayout11minimumSizeEv(const QFormLayout *self) {
  return new QSize(self->QFormLayout::minimumSize());
}

//  QSize QFormLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QFormLayout8sizeHintEv(const QFormLayout *self) {
  return new QSize(self->QFormLayout::sizeHint());
}

//  void QFormLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFormLayout10invalidateEv(QFormLayout *self) {
  self->QFormLayout::invalidate();
}

//  bool QFormLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFormLayout17hasHeightForWidthEv(
    const QFormLayout *self) {
  return self->QFormLayout::hasHeightForWidth();
}

//  int QFormLayout::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFormLayout14heightForWidthEi(
    const QFormLayout *self,
    int width) {
  return self->QFormLayout::heightForWidth(width);
}

//  Qt::Orientations QFormLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFormLayout19expandingDirectionsEv(
    const QFormLayout *self) {
  return static_cast<int>(self->QFormLayout::expandingDirections().toInt());
}

//  int QFormLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFormLayout5countEv(const QFormLayout *self) {
  return self->QFormLayout::count();
}
