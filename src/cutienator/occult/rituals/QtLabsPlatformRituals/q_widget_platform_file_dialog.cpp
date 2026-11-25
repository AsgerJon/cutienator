//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformfiledialog_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filedialog)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformfiledialog_p.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#include <QtGui/qwindow.h>

//  const QMetaObject *QWidgetPlatformFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QWidgetPlatformFileDialog10metaObjectEv(
    const QWidgetPlatformFileDialog *self) {
  return self->metaObject();
}

//  QWidgetPlatformFileDialog::~QWidgetPlatformFileDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialogD1Ev(
    QWidgetPlatformFileDialog *self) {
  delete self;
}

//  bool QWidgetPlatformFileDialog::defaultNameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QWidgetPlatformFileDialog25defaultNameFilterDisablesEv(
    const QWidgetPlatformFileDialog *self) {
  return self->defaultNameFilterDisables();
}

//  void QWidgetPlatformFileDialog::setDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialog12setDirectoryERK4QUrl(
    QWidgetPlatformFileDialog *self,
    const QUrl *directory) {
  self->setDirectory(*directory);
}

//  QUrl QWidgetPlatformFileDialog::directory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QWidgetPlatformFileDialog9directoryEv(
    const QWidgetPlatformFileDialog *self) {
  return new QUrl(self->directory());
}

//  void QWidgetPlatformFileDialog::selectFile(const QUrl &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialog10selectFileERK4QUrl(
    QWidgetPlatformFileDialog *self,
    const QUrl *filename) {
  self->selectFile(*filename);
}

//  QList<QUrl> QWidgetPlatformFileDialog::selectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK25QWidgetPlatformFileDialog13selectedFilesEv(
    const QWidgetPlatformFileDialog *self) {
  return new QList<QUrl>(self->selectedFiles());
}

//  void QWidgetPlatformFileDialog::setFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialog9setFilterEv(
    QWidgetPlatformFileDialog *self) {
  self->setFilter();
}

//  void QWidgetPlatformFileDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialog16selectNameFilterERK7QString(
    QWidgetPlatformFileDialog *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QString QWidgetPlatformFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWidgetPlatformFileDialog18selectedNameFilterEv(
    const QWidgetPlatformFileDialog *self) {
  return new QString(self->selectedNameFilter());
}

//  void QWidgetPlatformFileDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialog4execEv(
    QWidgetPlatformFileDialog *self) {
  self->exec();
}

//  bool QWidgetPlatformFileDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWidgetPlatformFileDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QWidgetPlatformFileDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags), modality, parent);
}

//  void QWidgetPlatformFileDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFileDialog4hideEv(
    QWidgetPlatformFileDialog *self) {
  self->hide();
}

#endif  // QT_CONFIG(filedialog)
