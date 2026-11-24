//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/rcc_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/rcc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "rcc_p.h"
#include <qbytearray.h>
#include <qdatetime.h>
#include <qdebug.h>
#include <qdir.h>
#include <qdiriterator.h>
#include <qfile.h>
#include <qiodevice.h>
#include <qlocale.h>
#include <qstack.h>
#include <qxmlstream.h>
#include <algorithm>
#if QT_CONFIG(zstd)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttools/src/designer/src/lib/shared/rcc.cpp, line 769, as _ZN18RCCResourceLibrary5resetEv
inline void RCCResourceLibrary::reset()
{
     if (m_root) {
        delete m_root;
        m_root = nullptr;
    }
    m_errorDevice = nullptr;
    m_failedResources.clear();
}

//  from ../qttools/src/designer/src/lib/shared/rcc.cpp, line 1325, as _ZN18RCCResourceLibrary28writeMangleNamespaceFunctionERK10QByteArray
inline void RCCResourceLibrary::writeMangleNamespaceFunction(const QByteArray &name)
{
    if (m_useNameSpace) {
        writeString("QT_RCC_MANGLE_NAMESPACE(");
        writeByteArray(name);
        writeChar(')');
    } else {
        writeByteArray(name);
    }
}

//  from ../qttools/src/designer/src/lib/shared/rcc.cpp, line 1336, as _ZN18RCCResourceLibrary25writeAddNamespaceFunctionERK10QByteArray
inline void RCCResourceLibrary::writeAddNamespaceFunction(const QByteArray &name)
{
    if (m_useNameSpace) {
        writeString("QT_RCC_PREPEND_NAMESPACE(");
        writeByteArray(name);
        writeChar(')');
    } else {
        writeByteArray(name);
    }
}

//  from ../qttools/src/designer/src/lib/shared/rcc.cpp, line 986, as _ZN18RCCResourceLibrary12writeDecimalEi
inline void RCCResourceLibrary::writeDecimal(int value)
{
    Q_ASSERT(m_format != RCCResourceLibrary::Binary);
    char buf[std::numeric_limits<int>::digits10 + 2];
    int n = snprintf(buf, sizeof(buf), "%d", value);
    write(buf, n);
}

//  from ../qttools/src/designer/src/lib/shared/rcc.cpp, line 46, as _ZN18RCCResourceLibrary14writeByteArrayERK10QByteArray
inline void RCCResourceLibrary::writeByteArray(const QByteArray &other)
{
    if (m_format == Pass2) {
        m_outDevice->write(other);
    } else {
        m_out.append(other);
    }
}

//  from ../qttools/src/designer/src/lib/shared/rcc.cpp, line 39, as _ZN18RCCResourceLibrary5writeEPKci
inline void RCCResourceLibrary::write(const char *str, int len)
{
    int n = m_out.size();
    m_out.resize(n + len);
    memcpy(m_out.data() + n, str, len);
}
//  -----------------------------------------------------------------------

//  void RCCResourceLibrary::setFormat(Format f)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary9setFormatENS_6FormatE(
    RCCResourceLibrary *self,
    RCCResourceLibrary::Format f) {
  self->setFormat(f);
}

//  Format RCCResourceLibrary::format() const
extern "C" Q_DECL_EXPORT
RCCResourceLibrary::Format ritual_ZNK18RCCResourceLibrary6formatEv(
    const RCCResourceLibrary *self) {
  return self->format();
}

//  void RCCResourceLibrary::setInputFiles(const QStringList &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary13setInputFilesERK5QListI7QStringE(
    RCCResourceLibrary *self,
    const QList<QString> *files) {
  self->setInputFiles(*files);
}

//  QStringList RCCResourceLibrary::inputFiles() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18RCCResourceLibrary10inputFilesEv(
    const RCCResourceLibrary *self) {
  return new QList<QString>(self->inputFiles());
}

//  void RCCResourceLibrary::setVerbose(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary10setVerboseEb(
    RCCResourceLibrary *self,
    bool b) {
  self->setVerbose(b);
}

//  bool RCCResourceLibrary::verbose() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18RCCResourceLibrary7verboseEv(
    const RCCResourceLibrary *self) {
  return self->verbose();
}

//  void RCCResourceLibrary::setInitName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary11setInitNameERK7QString(
    RCCResourceLibrary *self,
    const QString *name) {
  self->setInitName(*name);
}

//  QString RCCResourceLibrary::initName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18RCCResourceLibrary8initNameEv(
    const RCCResourceLibrary *self) {
  return new QString(self->initName());
}

//  void RCCResourceLibrary::setOutputName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary13setOutputNameERK7QString(
    RCCResourceLibrary *self,
    const QString *name) {
  self->setOutputName(*name);
}

//  QString RCCResourceLibrary::outputName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18RCCResourceLibrary10outputNameEv(
    const RCCResourceLibrary *self) {
  return new QString(self->outputName());
}

//  void RCCResourceLibrary::setCompressionAlgorithm(CompressionAlgorithm
//      algo)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary23setCompressionAlgorithmENS_20CompressionAlgorithmE(
    RCCResourceLibrary *self,
    RCCResourceLibrary::CompressionAlgorithm algo) {
  self->setCompressionAlgorithm(algo);
}

//  CompressionAlgorithm RCCResourceLibrary::compressionAlgorithm() const
extern "C" Q_DECL_EXPORT
RCCResourceLibrary::CompressionAlgorithm ritual_ZNK18RCCResourceLibrary20compressionAlgorithmEv(
    const RCCResourceLibrary *self) {
  return self->compressionAlgorithm();
}

//  void RCCResourceLibrary::setCompressLevel(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary16setCompressLevelEi(
    RCCResourceLibrary *self,
    int c) {
  self->setCompressLevel(c);
}

//  int RCCResourceLibrary::compressLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18RCCResourceLibrary13compressLevelEv(
    const RCCResourceLibrary *self) {
  return self->compressLevel();
}

//  void RCCResourceLibrary::setCompressThreshold(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary20setCompressThresholdEi(
    RCCResourceLibrary *self,
    int t) {
  self->setCompressThreshold(t);
}

//  int RCCResourceLibrary::compressThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18RCCResourceLibrary17compressThresholdEv(
    const RCCResourceLibrary *self) {
  return self->compressThreshold();
}

//  void RCCResourceLibrary::setResourceRoot(const QString &root)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary15setResourceRootERK7QString(
    RCCResourceLibrary *self,
    const QString *root) {
  self->setResourceRoot(*root);
}

//  QString RCCResourceLibrary::resourceRoot() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18RCCResourceLibrary12resourceRootEv(
    const RCCResourceLibrary *self) {
  return new QString(self->resourceRoot());
}

//  void RCCResourceLibrary::setUseNameSpace(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary15setUseNameSpaceEb(
    RCCResourceLibrary *self,
    bool v) {
  self->setUseNameSpace(v);
}

//  bool RCCResourceLibrary::useNameSpace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18RCCResourceLibrary12useNameSpaceEv(
    const RCCResourceLibrary *self) {
  return self->useNameSpace();
}

//  QStringList RCCResourceLibrary::failedResources() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18RCCResourceLibrary15failedResourcesEv(
    const RCCResourceLibrary *self) {
  return new QList<QString>(self->failedResources());
}

//  int RCCResourceLibrary::formatVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18RCCResourceLibrary13formatVersionEv(
    const RCCResourceLibrary *self) {
  return self->formatVersion();
}

//  void RCCResourceLibrary::setNoZstd(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary9setNoZstdEb(
    RCCResourceLibrary *self,
    bool v) {
  self->setNoZstd(v);
}

//  bool RCCResourceLibrary::noZstd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18RCCResourceLibrary6noZstdEv(
    const RCCResourceLibrary *self) {
  return self->noZstd();
}

//  void RCCResourceLibrary::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary5resetEv(RCCResourceLibrary *self) {
  self->reset();
}

//  void RCCResourceLibrary::writeMangleNamespaceFunction(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary28writeMangleNamespaceFunctionERK10QByteArray(
    RCCResourceLibrary *self,
    const QByteArray *name) {
  self->writeMangleNamespaceFunction(*name);
}

//  void RCCResourceLibrary::writeAddNamespaceFunction(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary25writeAddNamespaceFunctionERK10QByteArray(
    RCCResourceLibrary *self,
    const QByteArray *name) {
  self->writeAddNamespaceFunction(*name);
}

//  void RCCResourceLibrary::writeDecimal(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary12writeDecimalEi(
    RCCResourceLibrary *self,
    int value) {
  self->writeDecimal(value);
}

//  void RCCResourceLibrary::writeChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary9writeCharEc(
    RCCResourceLibrary *self,
    char c) {
  self->writeChar(c);
}

//  void RCCResourceLibrary::writeByteArray(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary14writeByteArrayERK10QByteArray(
    RCCResourceLibrary *self,
    const QByteArray *a0) {
  self->writeByteArray(*a0);
}

//  void RCCResourceLibrary::write(const char *a0, int len)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary5writeEPKci(
    RCCResourceLibrary *self,
    const char *a0,
    int len) {
  self->write(a0, len);
}

//  void RCCResourceLibrary::writeString(const char *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18RCCResourceLibrary11writeStringEPKc(
    RCCResourceLibrary *self,
    const char *s) {
  self->writeString(s);
}
