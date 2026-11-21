//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qwizard.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>

//  const QMetaObject *QWizardPage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QWizardPage10metaObjectEv(
    const QWizardPage *self) {
  return self->metaObject();
}

//  QString QWizardPage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QWizardPage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWizardPage::tr(s, c, n));
}

//  QWizardPage::QWizardPage(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWizardPage *ritual_ZN11QWizardPageC1EP7QWidget(QWidget *parent) {
  return new QWizardPage(parent);
}

//  QWizardPage::~QWizardPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPageD1Ev(QWizardPage *self) {
  delete self;
}

//  void QWizardPage::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage8setTitleERK7QString(
    QWizardPage *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString QWizardPage::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QWizardPage5titleEv(const QWizardPage *self) {
  return new QString(self->title());
}

//  void QWizardPage::setSubTitle(const QString &subTitle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage11setSubTitleERK7QString(
    QWizardPage *self,
    const QString *subTitle) {
  self->setSubTitle(*subTitle);
}

//  QString QWizardPage::subTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QWizardPage8subTitleEv(const QWizardPage *self) {
  return new QString(self->subTitle());
}

//  void QWizardPage::setPixmap(QWizard::WizardPixmap which, const QPixmap
//      &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage9setPixmapEN7QWizard12WizardPixmapERK7QPixmap(
    QWizardPage *self,
    QWizard::WizardPixmap which,
    const QPixmap *pixmap) {
  self->setPixmap(which, *pixmap);
}

//  QPixmap QWizardPage::pixmap(QWizard::WizardPixmap which) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK11QWizardPage6pixmapEN7QWizard12WizardPixmapE(
    const QWizardPage *self,
    QWizard::WizardPixmap which) {
  return new QPixmap(self->pixmap(which));
}

//  void QWizardPage::setFinalPage(bool finalPage)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage12setFinalPageEb(
    QWizardPage *self,
    bool finalPage) {
  self->setFinalPage(finalPage);
}

//  bool QWizardPage::isFinalPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWizardPage11isFinalPageEv(const QWizardPage *self) {
  return self->isFinalPage();
}

//  void QWizardPage::setCommitPage(bool commitPage)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage13setCommitPageEb(
    QWizardPage *self,
    bool commitPage) {
  self->setCommitPage(commitPage);
}

//  bool QWizardPage::isCommitPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWizardPage12isCommitPageEv(const QWizardPage *self) {
  return self->isCommitPage();
}

//  void QWizardPage::setButtonText(QWizard::WizardButton which, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage13setButtonTextEN7QWizard12WizardButtonERK7QString(
    QWizardPage *self,
    QWizard::WizardButton which,
    const QString *text) {
  self->setButtonText(which, *text);
}

//  QString QWizardPage::buttonText(QWizard::WizardButton which) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QWizardPage10buttonTextEN7QWizard12WizardButtonE(
    const QWizardPage *self,
    QWizard::WizardButton which) {
  return new QString(self->buttonText(which));
}

//  void QWizardPage::initializePage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage14initializePageEv(QWizardPage *self) {
  self->initializePage();
}

//  void QWizardPage::cleanupPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage11cleanupPageEv(QWizardPage *self) {
  self->cleanupPage();
}

//  bool QWizardPage::validatePage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QWizardPage12validatePageEv(QWizardPage *self) {
  return self->validatePage();
}

//  bool QWizardPage::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWizardPage10isCompleteEv(const QWizardPage *self) {
  return self->isComplete();
}

//  int QWizardPage::nextId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWizardPage6nextIdEv(const QWizardPage *self) {
  return self->nextId();
}
