//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  QFileOpenEvent *QFileOpenEvent::clone() const
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_ZNK14QFileOpenEvent5cloneEv(
    const QFileOpenEvent *self) {
  return self->clone();
}

//  QFileOpenEvent::~QFileOpenEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFileOpenEventD1Ev(QFileOpenEvent *self) {
  delete self;
}

//  QFileOpenEvent::QFileOpenEvent(const QString &file)
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_ZN14QFileOpenEventC1ERK7QString(const QString *file) {
  return new QFileOpenEvent(*file);
}

//  QFileOpenEvent::QFileOpenEvent(const QUrl &url)
extern "C" Q_DECL_EXPORT
QFileOpenEvent *ritual_ZN14QFileOpenEventC1ERK4QUrl(const QUrl *url) {
  return new QFileOpenEvent(*url);
}

//  QString QFileOpenEvent::file() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QFileOpenEvent4fileEv(const QFileOpenEvent *self) {
  return new QString(self->file());
}

//  QUrl QFileOpenEvent::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QFileOpenEvent3urlEv(const QFileOpenEvent *self) {
  return new QUrl(self->url());
}
