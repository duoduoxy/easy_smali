.class public LTest;
.super Ljava/lang/Object;
.source "Test.java"

.method public constructor <init>()V
    .registers 1
    .prologue
    .line 1
    invoke-direct { p0 }, Ljava/lang/Object;-><init>()V
    return-void
.end method

.method public static main([Ljava/lang/String;)V
    .registers 3
    .prologue
    .line 3
    sget-object v0, Ljava/lang/System;->out:Ljava/io/PrintStream;
    const-string v1, "cbl"
    invoke-virtual { v0, v1 }, Ljava/io/PrintStream;->println(Ljava/lang/String;)V
    .line 4
    return-void
.end method
