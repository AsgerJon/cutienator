//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>

//  QSupportedWritingSystems::QSupportedWritingSystems()
extern "C" Q_DECL_EXPORT
QSupportedWritingSystems *ritual_ZN24QSupportedWritingSystemsC1Ev() {
  return new QSupportedWritingSystems();
}

//  QSupportedWritingSystems::QSupportedWritingSystems(const
//      QSupportedWritingSystems &other)
extern "C" Q_DECL_EXPORT
QSupportedWritingSystems *ritual_ZN24QSupportedWritingSystemsC1ERKS_(
    const QSupportedWritingSystems *other) {
  return new QSupportedWritingSystems(*other);
}

//  QSupportedWritingSystems &QSupportedWritingSystems::operator=(const
//      QSupportedWritingSystems &other)
extern "C" Q_DECL_EXPORT
QSupportedWritingSystems *ritual_ZN24QSupportedWritingSystemsaSERKS_(
    QSupportedWritingSystems *self,
    const QSupportedWritingSystems *other) {
  return &(self->operator=(*other));
}

//  QSupportedWritingSystems::~QSupportedWritingSystems()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSupportedWritingSystemsD1Ev(
    QSupportedWritingSystems *self) {
  delete self;
}

//  void QSupportedWritingSystems::setSupported(QFontDatabase::WritingSystem
//      a0, bool supported)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSupportedWritingSystems12setSupportedEN13QFontDatabase13WritingSystemEb(
    QSupportedWritingSystems *self,
    QFontDatabase::WritingSystem a0,
    bool supported) {
  self->setSupported(a0, supported);
}

//  bool QSupportedWritingSystems::supported(QFontDatabase::WritingSystem a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSupportedWritingSystems9supportedEN13QFontDatabase13WritingSystemE(
    const QSupportedWritingSystems *self,
    QFontDatabase::WritingSystem a0) {
  return self->supported(a0);
}

//  void QSupportedWritingSystems::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSupportedWritingSystems6detachEv(
    QSupportedWritingSystems *self) {
  self->detach();
}

//  bool operator==(const QSupportedWritingSystems &a0, const
//      QSupportedWritingSystems &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QSupportedWritingSystemsS1_(
    const QSupportedWritingSystems *a0,
    const QSupportedWritingSystems *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(const QSupportedWritingSystems &a0, const
//      QSupportedWritingSystems &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QSupportedWritingSystemsS1_(
    const QSupportedWritingSystems *a0,
    const QSupportedWritingSystems *a1) {
  return operator!=(*a0, *a1);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QSupportedWritingSystems &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK24QSupportedWritingSystems(
    const QDebug *a0,
    const QSupportedWritingSystems *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
