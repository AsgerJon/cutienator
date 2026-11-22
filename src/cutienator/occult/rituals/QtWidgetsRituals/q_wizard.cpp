//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qwizard.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QWizard::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QWizard10metaObjectEv(const QWizard *self) {
  return self->metaObject();
}

//  QString QWizard::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QWizard2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QWizard::tr(s, c, n));
}

//  QWizard::QWizard(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QWizard *ritual_ZN7QWizardC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new QWizard(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QWizard::~QWizard()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizardD1Ev(QWizard *self) {
  delete self;
}

//  int QWizard::addPage(QWizardPage *page)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QWizard7addPageEP11QWizardPage(
    QWizard *self,
    QWizardPage *page) {
  return self->addPage(page);
}

//  void QWizard::setPage(int id, QWizardPage *page)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard7setPageEiP11QWizardPage(
    QWizard *self,
    int id,
    QWizardPage *page) {
  self->setPage(id, page);
}

//  void QWizard::removePage(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10removePageEi(QWizard *self, int id) {
  self->removePage(id);
}

//  QWizardPage *QWizard::page(int id) const
extern "C" Q_DECL_EXPORT
QWizardPage *ritual_ZNK7QWizard4pageEi(const QWizard *self, int id) {
  return self->page(id);
}

//  bool QWizard::hasVisitedPage(int id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWizard14hasVisitedPageEi(const QWizard *self, int id) {
  return self->hasVisitedPage(id);
}

//  void QWizard::setStartId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10setStartIdEi(QWizard *self, int id) {
  self->setStartId(id);
}

//  int QWizard::startId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard7startIdEv(const QWizard *self) {
  return self->startId();
}

//  QWizardPage *QWizard::currentPage() const
extern "C" Q_DECL_EXPORT
QWizardPage *ritual_ZNK7QWizard11currentPageEv(const QWizard *self) {
  return self->currentPage();
}

//  int QWizard::currentId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard9currentIdEv(const QWizard *self) {
  return self->currentId();
}

//  bool QWizard::validateCurrentPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWizard19validateCurrentPageEv(QWizard *self) {
  return self->validateCurrentPage();
}

//  int QWizard::nextId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard6nextIdEv(const QWizard *self) {
  return self->nextId();
}

//  void QWizard::setField(const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard8setFieldERK7QStringRK8QVariant(
    QWizard *self,
    const QString *name,
    const QVariant *value) {
  self->setField(*name, *value);
}

//  QVariant QWizard::field(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QWizard5fieldERK7QString(
    const QWizard *self,
    const QString *name) {
  return new QVariant(self->field(*name));
}

//  void QWizard::setWizardStyle(WizardStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard14setWizardStyleENS_11WizardStyleE(
    QWizard *self,
    QWizard::WizardStyle style) {
  self->setWizardStyle(style);
}

//  WizardStyle QWizard::wizardStyle() const
extern "C" Q_DECL_EXPORT
QWizard::WizardStyle ritual_ZNK7QWizard11wizardStyleEv(const QWizard *self) {
  return self->wizardStyle();
}

//  void QWizard::setOption(WizardOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard9setOptionENS_12WizardOptionEb(
    QWizard *self,
    QWizard::WizardOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QWizard::testOption(WizardOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWizard10testOptionENS_12WizardOptionE(
    const QWizard *self,
    QWizard::WizardOption option) {
  return self->testOption(option);
}

//  void QWizard::setOptions(WizardOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10setOptionsE6QFlagsINS_12WizardOptionEE(
    QWizard *self,
    int options) {
  self->setOptions(QFlags<QWizard::WizardOption>::fromInt(options));
}

//  WizardOptions QWizard::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard7optionsEv(const QWizard *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QWizard::setButtonText(WizardButton which, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard13setButtonTextENS_12WizardButtonERK7QString(
    QWizard *self,
    QWizard::WizardButton which,
    const QString *text) {
  self->setButtonText(which, *text);
}

//  QString QWizard::buttonText(WizardButton which) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWizard10buttonTextENS_12WizardButtonE(
    const QWizard *self,
    QWizard::WizardButton which) {
  return new QString(self->buttonText(which));
}

//  void QWizard::setButton(WizardButton which, QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard9setButtonENS_12WizardButtonEP15QAbstractButton(
    QWizard *self,
    QWizard::WizardButton which,
    QAbstractButton *button) {
  self->setButton(which, button);
}

//  QAbstractButton *QWizard::button(WizardButton which) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK7QWizard6buttonENS_12WizardButtonE(
    const QWizard *self,
    QWizard::WizardButton which) {
  return self->button(which);
}

//  void QWizard::setTitleFormat(Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard14setTitleFormatEN2Qt10TextFormatE(
    QWizard *self,
    Qt::TextFormat format) {
  self->setTitleFormat(format);
}

//  Qt::TextFormat QWizard::titleFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK7QWizard11titleFormatEv(const QWizard *self) {
  return self->titleFormat();
}

//  void QWizard::setSubTitleFormat(Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard17setSubTitleFormatEN2Qt10TextFormatE(
    QWizard *self,
    Qt::TextFormat format) {
  self->setSubTitleFormat(format);
}

//  Qt::TextFormat QWizard::subTitleFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK7QWizard14subTitleFormatEv(const QWizard *self) {
  return self->subTitleFormat();
}

//  void QWizard::setPixmap(WizardPixmap which, const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard9setPixmapENS_12WizardPixmapERK7QPixmap(
    QWizard *self,
    QWizard::WizardPixmap which,
    const QPixmap *pixmap) {
  self->setPixmap(which, *pixmap);
}

//  QPixmap QWizard::pixmap(WizardPixmap which) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QWizard6pixmapENS_12WizardPixmapE(
    const QWizard *self,
    QWizard::WizardPixmap which) {
  return new QPixmap(self->pixmap(which));
}

//  void QWizard::setSideWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard13setSideWidgetEP7QWidget(
    QWizard *self,
    QWidget *widget) {
  self->setSideWidget(widget);
}

//  QWidget *QWizard::sideWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWizard10sideWidgetEv(const QWizard *self) {
  return self->sideWidget();
}

//  void QWizard::setDefaultProperty(const char *className, const char
//      *property, const char *changedSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard18setDefaultPropertyEPKcS1_S1_(
    QWizard *self,
    const char *className,
    const char *property,
    const char *changedSignal) {
  self->setDefaultProperty(className, property, changedSignal);
}

//  void QWizard::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10setVisibleEb(QWizard *self, bool visible) {
  self->setVisible(visible);
}

//  QSize QWizard::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWizard8sizeHintEv(const QWizard *self) {
  return new QSize(self->sizeHint());
}

//  void QWizard::back()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard4backEv(QWizard *self) {
  self->back();
}

//  void QWizard::next()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard4nextEv(QWizard *self) {
  self->next();
}

//  void QWizard::setCurrentId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard12setCurrentIdEi(QWizard *self, int id) {
  self->setCurrentId(id);
}

//  void QWizard::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard7restartEv(QWizard *self) {
  self->restart();
}
