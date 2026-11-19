//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgroupbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgroupbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QGroupBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QGroupBox10metaObjectEv(
    const QGroupBox *self) {
  return self->metaObject();
}

//  QString QGroupBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QGroupBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGroupBox::tr(s, c, n));
}

//  QGroupBox::QGroupBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QGroupBox *ritual_ZN9QGroupBoxC1EP7QWidget(QWidget *parent) {
  return new QGroupBox(parent);
}

//  QGroupBox::QGroupBox(const QString &title, QWidget *parent)
extern "C" Q_DECL_EXPORT
QGroupBox *ritual_ZN9QGroupBoxC1ERK7QStringP7QWidget(
    const QString *title,
    QWidget *parent) {
  return new QGroupBox(*title, parent);
}

//  QGroupBox::~QGroupBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBoxD1Ev(QGroupBox *self) {
  delete self;
}

//  QString QGroupBox::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QGroupBox5titleEv(const QGroupBox *self) {
  return new QString(self->title());
}

//  void QGroupBox::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox8setTitleERK7QString(
    QGroupBox *self,
    const QString *title) {
  self->setTitle(*title);
}

//  Qt::Alignment QGroupBox::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QGroupBox9alignmentEv(const QGroupBox *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QGroupBox::setAlignment(int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox12setAlignmentEi(QGroupBox *self, int alignment) {
  self->setAlignment(alignment);
}

//  QSize QGroupBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QGroupBox15minimumSizeHintEv(const QGroupBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  bool QGroupBox::isFlat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGroupBox6isFlatEv(const QGroupBox *self) {
  return self->isFlat();
}

//  void QGroupBox::setFlat(bool flat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox7setFlatEb(QGroupBox *self, bool flat) {
  self->setFlat(flat);
}

//  bool QGroupBox::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGroupBox11isCheckableEv(const QGroupBox *self) {
  return self->isCheckable();
}

//  void QGroupBox::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox12setCheckableEb(QGroupBox *self, bool checkable) {
  self->setCheckable(checkable);
}

//  bool QGroupBox::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGroupBox9isCheckedEv(const QGroupBox *self) {
  return self->isChecked();
}

//  void QGroupBox::setChecked(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox10setCheckedEb(QGroupBox *self, bool checked) {
  self->setChecked(checked);
}
