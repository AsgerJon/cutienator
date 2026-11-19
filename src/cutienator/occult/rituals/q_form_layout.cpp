//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qformlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qformlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

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
  return new QFormLayout(parent);
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
