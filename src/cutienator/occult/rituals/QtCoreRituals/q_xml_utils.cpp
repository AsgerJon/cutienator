//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qxmlutils_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qxmlutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>

//  bool QXmlUtils::isEncName(QStringView encName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils9isEncNameE11QStringView(const QString *encName) {
  return QXmlUtils::isEncName(QStringView(*encName));
}

//  bool QXmlUtils::isNameChar(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils10isNameCharE5QChar(const QChar *c) {
  return QXmlUtils::isNameChar(*c);
}

//  bool QXmlUtils::isLetter(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils8isLetterE5QChar(const QChar *c) {
  return QXmlUtils::isLetter(*c);
}

//  bool QXmlUtils::isNCName(QStringView ncName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils8isNCNameE11QStringView(const QString *ncName) {
  return QXmlUtils::isNCName(QStringView(*ncName));
}

//  bool QXmlUtils::isPublicID(QStringView candidate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils10isPublicIDE11QStringView(
    const QString *candidate) {
  return QXmlUtils::isPublicID(QStringView(*candidate));
}

//  bool QXmlUtils::isBaseChar(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils10isBaseCharE5QChar(const QChar *c) {
  return QXmlUtils::isBaseChar(*c);
}

//  bool QXmlUtils::isDigit(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils7isDigitE5QChar(const QChar *c) {
  return QXmlUtils::isDigit(*c);
}

//  bool QXmlUtils::isExtender(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils10isExtenderE5QChar(const QChar *c) {
  return QXmlUtils::isExtender(*c);
}

//  bool QXmlUtils::isIdeographic(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils13isIdeographicE5QChar(const QChar *c) {
  return QXmlUtils::isIdeographic(*c);
}

//  bool QXmlUtils::isCombiningChar(const QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXmlUtils15isCombiningCharE5QChar(const QChar *c) {
  return QXmlUtils::isCombiningChar(*c);
}

//  QXmlUtils::~QXmlUtils()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXmlUtilsD1Ev(QXmlUtils *self) {
  delete self;
}
